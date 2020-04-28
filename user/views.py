from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from dal import autocomplete

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

class UserProfileAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Country.objects.none()

        qs = UserProfile.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs