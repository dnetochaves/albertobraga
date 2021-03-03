
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from apps.user_profile.models import UserProfile


class AccountView(TemplateView):
    template_name = "user_profile/account.html"


class UserProfileUpdate(UpdateView):
    model = UserProfile
    fields = ['name']
