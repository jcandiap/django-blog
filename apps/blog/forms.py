from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from blog.models import BlogUser

class RegisterBlogUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    confirmEmail = forms.EmailField(label='Confirmar correo electrónico', required=True)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = BlogUser
        fields = ['first_name', 'last_name', 'username', 'email', 'confirmEmail', 'password1', 'password2', 'avatar']