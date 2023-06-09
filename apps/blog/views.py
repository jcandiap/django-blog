from django.shortcuts import render, redirect
from django.db.models import Q
from .controllers.user_controller import auth_login
from .forms import RegisterBlogUserForm, PostForm, CommentForm
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
app_name = 'blog'

def index(request, message = None, undefined_url=None):
    if undefined_url is not None:
        return redirect('blog:index')
    search = request.GET.get('search')
    if search:
        post_list = models.Post.objects.filter(Q(title__icontains=search) | Q(content__icontains=search)).order_by('-publish_date')
    else:
        post_list = models.Post.objects.all().order_by('-publish_date')
    for post in post_list:
        post.commets = models.Comment.objects.filter(post=post).count()
        post.votes = models.Vote.objects.filter(post=post).count()
        if request.user.is_authenticated:
            vote = models.Vote.objects.filter(post=post, user=request.user)
            if vote:
                post.vote = True
    return render(request, 'blog/index.html', { 'post_list': post_list, 'message': message })

def submit(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('blog:register')
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            print(post)
            return redirect('blog:index')
        errores = []
        for field, error_msgs in form.errors.items():
            for error_msg in error_msgs:
                errores.append(f"{error_msg}")
        return render(request, 'blog/register.html', { 'error': errores, 'form': form.data })
    return render(request, 'blog/submit.html')


# Register:::


def register(request):
    if request.method == 'GET':
        return render(request, 'blog/register.html')
    elif request.method == 'POST':
        form = RegisterBlogUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('blog:index') 
        errores = []
        for field, error_msgs in form.errors.items():
            for error_msg in error_msgs:
                errores.append(f"{error_msg}")
        return render(request, 'blog/register.html', { 'error': errores, 'form': form.data })
    else:
        return render(request, 'blog/register.html')

# Login:::
from .controllers.user_controller import check_user_login

def login(request):
    if request.method == 'POST':
        try:
            if check_user_login(request):
                return redirect('blog:index')
            else:
                return render(request, 'blog/register.html', { 
                    'status': 'error', 
                    'message': 'Usuario ingresado no se encuentra registrado\n Intentalo nuevamente, de lo contrario, registrate! 👀' 
                })
        except Exception as ex:
            return redirect('blog:index')
    else:
        return redirect('blog:index')
    
@login_required
def profile(request):
    try:
        votes = models.Vote.objects.filter(user=request.user).count()
        posts = models.Post.objects.filter(author=request.user).count()
    except Exception as e:
        print(e)
    return render(request, 'blog/profile.html', { 'post_count': posts, 'likes_count': votes })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        if avatar:
            user.avatar = avatar
        user.save()
        return redirect('blog:profile')
    return render(request, 'blog/edit_profile.html')
    
def post_detail(request):
    try:
        id = request.GET.get('id')
        post = models.Post.objects.get(id=id)
        if post:
            comments = models.Comment.objects.filter(post = post)
            post.commets = models.Comment.objects.filter(post=post).count()
            post.votes = models.Vote.objects.filter(post=post)
            if request.user.is_authenticated:
                vote = models.Vote.objects.filter(post=post, user=request.user)
                if vote:
                    post.vote = True
            return render(request, 'blog/post_detail.html', { 'post': post, 'comments': comments })
        else:
            return redirect('blog:index')
    except Exception as e:
        print(e)
        return redirect('blog:index')
    
def like_post(request):
    referer = request.META.get('HTTP_REFERER')
    try:
        if request.user.is_authenticated:
            id = request.GET.get('id')
            post = models.Post.objects.filter(id = id).first()
            vote_verification = models.Vote.objects.filter(post = post, user = request.user).first()
            if vote_verification is None:
                vote = models.Vote(user=request.user, post=post)
                vote.save()
            else:
                vote_verification.delete()
            return redirect(referer)
        else:
            return redirect('blog:register')
    except Exception as e:
        print(e)
        return redirect('blog:index')
    
def comment_post(request):
    referer = request.META.get('HTTP_REFERER')
    try:
        if request.user.is_authenticated and request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                form_info = form.cleaned_data
                post = models.Post.objects.filter(id=form_info['post']).first()
                comment = models.Comment(content=form_info['content'], author=request.user, post=post)
                comment.save()
        else:
            return redirect('blog:register')
    except Exception as e:
        print(e)
    return redirect(referer)

def delete_comment(request):
    referer = request.META.get('HTTP_REFERER')
    try:
        id = request.GET.get('id')
        comment = models.Comment.objects.get(id = id)
        if request.user.is_authenticated and comment:
            comment.delete()
    except Exception as e:
        print(e)
    return redirect(referer)

def delete_post(request):
    try:
        id = request.GET.get('id')
        post = models.Post.objects.get(id = id)
        if request.user.is_authenticated and post and post.author == request.user:
            post.delete()
            return index(request, { 'success': 'Publicación eliminada con exito!' })
        else:
            return index(request, { 'error': 'No cumple con las condiciones para poder eliminar esta publicación!' })
    except Exception as e:
        print(e)
        return index(request, { 'error': 'Ocurrio un error al intentar eliminar la publicación!' })
    
def about(request):
    return render(request, 'blog/about.html')