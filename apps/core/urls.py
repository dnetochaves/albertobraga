from django.urls import path, include
from . import views

app_name = "core"

urlpatterns = [
    path('', views.CoreView.as_view()),
    path('nosso-vereador', views.NossoVereadorView.as_view(), name='nosso-vereador'),
    path('time', views.TimeView.as_view(), name='time'),
    path('testemunhos', views.TestemunhosView.as_view(), name='testemunhos'),
    #path('blog', views.BlogView.as_view(), name='blog'),
    path('contato', views.ContatoView.as_view(), name='contato'),
]
