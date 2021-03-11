from django.db import models
from django.contrib.auth.models import User

class Categorias(models.Model):
    nome = models.CharField(, max_length=50)


class Tags(models.Model):
    nome = models.CharField(max_length=50)


class Noticias(models.Model):
    imagem = models.ImageField(
        upload_to='blog', height_field=None, width_field=None, max_length=None)
    titulo = models.CharField(max_length=100)
    responsavel = models.ForeignKey(User, on_delete=models.PROTECT)
    data = models.DateField(auto_now=False, auto_now_add=True)
    conteudo = models.TextField()
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    tags = models.ForeignKey(Tags, on_delete=models.PROTECT)
