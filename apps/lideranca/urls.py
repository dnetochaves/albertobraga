from django.urls import path, include
from . import views

app_name = "lideranca"

urlpatterns = [
    path('list-lideranca', views.lideranca_list, name='list-lideranca'),
    path('lideranca-create', views.LiderancaCreate.as_view(),
         name='lideranca-create'),
    path('lideranca-list/', views.ListLideranca.as_view(),
         name='lideranca-list'),
    path('lideranca-update/<int:pk>/', views.LiderancaUpdate.as_view(),
         name='lideranca-update'),
    path('lideranca-delete/<int:pk>/', views.LiderancaDelete.as_view(),
         name='lideranca-delete'),

]
