from django.urls import path
from blog import views
from django.contrib.auth.views import LogoutView

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('submit', views.submit, name='submit'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', LogoutView.as_view(template_name='blog/index.html'), name='logout'),
    path('post', views.post_detail, name='post'),
    path('like_post', views.like_post, name='like_post'),
    path('comment_post', views.comment_post, name='comment_post'),
    path('delete_comment', views.delete_comment, name='delete_comment')
]
