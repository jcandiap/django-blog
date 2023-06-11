from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from blog.models import BlogUser

class RegisterBlogUserForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True)
    lastName = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    confirmEmail = forms.EmailField(label='Confirmar correo electrónico', required=True)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = BlogUser
        fields = ['name', 'lastName', 'username', 'email', 'confirmEmail', 'password1', 'password2', 'avatar']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        email = cleaned_data.get('email')
        confirmEmail = cleaned_data.get('confirmEmail')

        # Validar que las contraseñas coincidan
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Las contraseñas no coinciden')

        # Validar que los correos electrónicos coincidan
        if email and confirmEmail and email != confirmEmail:
            self.add_error('confirmEmail', 'Los correos electrónicos no coinciden')