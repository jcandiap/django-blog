from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
app_name = 'blog'

def index(request):
    return render(request, 'blog/index.html')

def submit(request):
    return render(request, 'blog/submit.html')


# Register:::
from .forms import RegisterBlogUserForm

def register(request):
    if request.method == 'GET':
        return render(request, 'blog/register.html')
    elif request.method == 'POST':
        form = RegisterBlogUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
        field_error = form.errors
        return render(request, 'blog/register.html', { 'error': field_error, 'form': form.data })
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