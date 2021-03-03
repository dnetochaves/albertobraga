from django.urls import path, include
from . import views

app_name = "core"

urlpatterns = [
    path('index/', views.CoreView.as_view()),
]