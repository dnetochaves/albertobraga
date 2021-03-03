from django.db import models
from django.urls import reverse


class Lideranca(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    data_nascimento = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('lideranca:list-lideranca')
    

