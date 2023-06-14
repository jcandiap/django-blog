from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user
from blog.models import BlogUser, Post

class RegisterBlogUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    confirmEmail = forms.EmailField(label='Confirmar correo electrónico', required=True)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = BlogUser
        fields = ['first_name', 'last_name', 'username', 'email', 'confirmEmail', 'password1', 'password2', 'avatar']
        
class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=300, required=True)
    content = forms.CharField(max_length=1000, required=True)
    image = forms.ImageField(required=False)
    author = forms.Field(required=False)
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'image']
        
class CommentForm(forms.Form):
    content = forms.CharField(max_length=1000, required=True)
    post = forms.CharField(required=True)