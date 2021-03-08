from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


class CoreView(TemplateView):
    template_name = "core/index.html"


class NossoVereadorView(TemplateView):
    template_name = "core/nosso-vereador.html"


class TimeView(TemplateView):
    template_name = "core/time.html"


class TestemunhosView(TemplateView):
    template_name = "core/testemunhos.html"


class BlogView(TemplateView):
    template_name = "core/blog.html"


class ContatoView(TemplateView):
    template_name = "core/contato.html"
