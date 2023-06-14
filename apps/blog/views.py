from django.shortcuts import render, redirect
from .controllers.user_controller import auth_login
from .forms import RegisterBlogUserForm, PostForm
from . import models
import json

# Create your views here.
app_name = 'blog'

def index(request):
    post_list = models.Post.objects.all().order_by('-publish_date')
    for post in post_list:
        post.commets = models.Comment.objects.filter(post=post).count()
        post.votes = models.Vote.objects.filter(post=post).count()
        if request.user.is_authenticated:
            vote = models.Vote.objects.filter(post=post, user=request.user)
            if vote:
                post.vote = True
    return render(request, 'blog/index.html', { 'post_list': post_list })

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
    
def post_detail(request):
    try:
        id = request.GET.get('id')
        post = models.Post.objects.get(id=id)
        if post:
            comments = models.Comment.objects.filter(post = post)
            post.votes = models.Vote.objects.filter(post=post).count()
            return render(request, 'blog/post_detail.html', { 'post': post, 'comments': comments })
        else:
            return redirect('blog:index')
    except Exception as e:
        print(e)
        return redirect('blog:index')
    
def like_post(request):
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
            return redirect('blog:index')
        else:
            return redirect('blog:register')
    except Exception as e:
        print(e)
        return redirect('blog:index')
    
def comment_post(request):
    try:
        if request.user.is_authenticated and request.method == "POST":
            print('XD')
    except Exception as e:
        print(e)