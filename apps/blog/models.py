from django.db import models
from django.contrib.auth.models import User

def upload_to(instance, filename):
    return f'blog/{instance.author.username}/{filename}'

class Image(models.Model):
    image = models.ImageField(upload_to=upload_to)
    
    def __str__(self):
        return self.image.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Vote(models.Model):
    VOTE_TYPE = (
        ('positivo', 'Positivo'),
        ('negativo', 'Negativo'),
    )
    type = models.CharField(max_length=10, choices=VOTE_TYPE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.type} voto por {self.user}"

class Tag(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.name
