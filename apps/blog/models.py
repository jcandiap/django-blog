from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid

def upload_to(instance, filename):
    return f'blog/{instance.author.username}/{filename}'

class BlogUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='blog_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='blog_users', blank=True)
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    image = models.ImageField(upload_to=upload_to, null=True)

    def __str__(self):
        return self.title
    
class BlogGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(BlogUser, on_delete=models.CASCADE, related_name='created_groups')
    posts = models.ManyToManyField(Post)
    members = models.ManyToManyField(BlogUser, related_name='joined_groups')
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Vote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.user} voto por {self.post}"

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.name
