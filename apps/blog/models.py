from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

def upload_to(instance, filename):
    return f'blog/{instance.author.username}/{filename}'

class BlogUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='blog_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='blog_users', blank=True)
    
class Avatar(models.Model):
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

class Image(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, editable=False)
    image = models.ImageField(upload_to=upload_to)
    
    def __str__(self):
        return self.image.name

class Post(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.title
    
class BlogGroup(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, editable=False)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(BlogUser, on_delete=models.CASCADE, related_name='created_groups')
    posts = models.ManyToManyField(Post)
    members = models.ManyToManyField(BlogUser, related_name='joined_groups')
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, editable=False)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Vote(models.Model):
    VOTE_TYPE = (
        ('positivo', 'Positivo'),
        ('negativo', 'Negativo'),
    )
    type = models.CharField(max_length=10, choices=VOTE_TYPE)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.type} voto por {self.user}"

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.name
