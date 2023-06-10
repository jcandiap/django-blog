from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
app_name = 'blog'

def index(request):
    return render(request, 'blog/index.html')

def submit(request):
    return render(request, 'blog/submit.html')


# Register:::
def register(request):
    if request.method == 'GET':
        return render(request, 'blog/register.html')
    elif request.method == 'POST':
        return render(request, 'blog/register.html')
    else:
        return render(request, 'blog/register.html')


# Login:::
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        try:
            form = AuthenticationForm(request.POST, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                print('USER:::', user)
                if user is not None:
                    auth_login(request, user)
                    return JsonResponse({ 'message': f'Bienvenido/a, {user.get_username()}' })
            else:
                return JsonResponse({ 'error': 'Usuario ingresado no es valido!' })
        except Exception as ex:
            print(ex)
            return render(request, 'blog/index.html')