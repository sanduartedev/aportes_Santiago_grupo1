from django.db import models
#FAQ
import datetime
from django.utils import timezone

#Noticia
from django.conf import settings


# Para el mapa
class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

# Question
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField("date_published")

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# Institucional
class Personal(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    cargo = models.TextField(null=True,verbose_name='Cargo')
    foto = models.ImageField(upload_to='static/img/',null=True,verbose_name='Foto')
    def __str__(self):
        return self.nombre, self.cargo, self.foto

#Noticia

class Noticia(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        