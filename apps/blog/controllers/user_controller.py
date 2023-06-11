from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from blog.forms import RegisterBlogUserForm

def check_user_login(request):
    try:
        form = AuthenticationForm(request.POST, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return True
            else: 
                return False
    except Exception as e:
        raise Exception(f'Error al validar el formulario [{ e }]')
    
def register_user(request):
    try:
        if request.method == 'POST':
            form = RegisterBlogUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
    except:
        raise Exception(f'')