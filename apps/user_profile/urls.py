
from django.urls import path, include
from . import views

app_name = "user_profile"

urlpatterns = [
    path('account/', views.AccountView.as_view(), name='account'),
    path('account-update/<int:pk>/',  views.UserProfileUpdate.as_view(), name='account-update'),
]