from django.urls import path
from blog import views
from django.contrib.auth.views import LogoutView

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('submit', views.submit, name='submit'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', LogoutView.as_view(template_name='blog/index.html'), name='logout')
]
