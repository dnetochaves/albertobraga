from django.urls import path, include
from . import views

app_name = "lideranca"

urlpatterns = [
    path('list-lideranca', views.lideranca_list, name='list-lideranca'),

]