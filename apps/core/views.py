
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


class CoreView(TemplateView):
    template_name = "core/index.html"