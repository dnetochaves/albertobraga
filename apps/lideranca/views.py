from django.shortcuts import render
from django.views.generic.list import ListView
from apps.lideranca.models import Lideranca
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView


def lideranca_list(request):
    liderancas = Lideranca.objects.all()
    return render(request, 'lideranca/lideranca_list1.html', {'liderancas': liderancas})


class LiderancaCreate(CreateView):
    model = Lideranca
    fields = ['nome', 'telefone', 'data_nascimento']

class ListLideranca(ListView):
    model = Lideranca

