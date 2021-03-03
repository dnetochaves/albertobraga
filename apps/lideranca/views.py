from django.shortcuts import render
from django.views.generic.list import ListView
from apps.lideranca.models import Lideranca
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


def lideranca_list(request):
    liderancas = Lideranca.objects.all()
    return render(request, 'lideranca/lideranca_list1.html', {'liderancas': liderancas})


class LiderancaCreate(SuccessMessageMixin, CreateView):
    model = Lideranca
    fields = ['nome', 'telefone', 'data_nascimento']
    success_message = "%(nome)s criado com sucesso"


class ListLideranca(ListView):
    model = Lideranca


class LiderancaUpdate(UpdateView):
    model = Lideranca
    fields = ['nome', 'telefone', 'data_nascimento']


class LiderancaDelete(DeleteView):
    model = Lideranca
    fields = ['nome', 'telefone', 'data_nascimento']
    success_url = reverse_lazy('lideranca:lideranca-list')
