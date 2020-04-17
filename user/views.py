from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from user.models import UserProfile
from user.forms import UserProfileForm


class UserProfileList(ListView):
    model = UserProfile


class UserProfileCreate(CreateView):
    model = UserProfile
    form_class = UserProfileForm


class UserProfileUpdate(UpdateView):
    model = UserProfile
    form_class = UserProfileForm


class UserProfileDelete(DeleteView):
    model = UserProfile
    success_url = reverse_lazy('profiles')