from django.http import JsonResponse
from django.shortcuts import render, redirect
from .controllers.user_controller import auth_login
from .forms import RegisterBlogUserForm, PostForm

# Create your views here.
app_name = 'blog'

def index(request):
    return render(request, 'blog/index.html')

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