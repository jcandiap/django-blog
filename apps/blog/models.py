from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.contenido

class Vote(models.Model):
    TIPO_VOTO = (
        ('positivo', 'Positivo'),
        ('negativo', 'Negativo'),
    )
    tipo = models.CharField(max_length=10, choices=TIPO_VOTO)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    comentario = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} voto por {self.usuario}"

class Tag(models.Model):
    nombre = models.CharField(max_length=50)
    publicaciones = models.ManyToManyField(Post)

    def __str__(self):
        return self.nombre
