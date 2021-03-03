from django.shortcuts import render
from django.views.generic.list import ListView
from apps.lideranca.models import Lideranca
from django.views.generic import TemplateView
from django.http import HttpResponse

class LiderancaView(TemplateView):
    template_name = "lideranca/index.html"

def teste_rota(request):
    return HttpResponse("Teste de rota")

def lideranca_list(request):
    liderancas = Lideranca.objects.all()
    return render(request, 'lideranca/lideranca_list.html', {'liderancas': liderancas})