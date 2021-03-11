from django.shortcuts import render
from django.views.generic.list import ListView
from . models import Noticias, Categorias, Tags


class BlogListView(ListView):

    model = Noticias
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categorias.objects.all()
        context['tags'] = Tags.objects.all()
        return context
