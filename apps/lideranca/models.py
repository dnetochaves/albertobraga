from django.db import models

class Lideranca(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    data_nascimento = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nome
    

