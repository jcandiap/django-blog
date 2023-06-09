from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
app_name = 'blog'

def index(request):
    return render(request, 'blog/index.html')

def submit(request):
    return render(request, 'blog/submit.html')

def register(request):
    return render(request, 'blog/register.html')




# Login:::
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    print('paso por aqui!')
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'blog/index.html', { 'message': f'Bienvenido/a, { user.get_username() }'})
        else:
            return JsonResponse({ 'error': 'Usuario ingresado no es valido!' })