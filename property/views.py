from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from property.models import Device, Material
from property.forms import DeviceForm, MaterialForm


class DeviceList(ListView):
    model = Device


class DeviceCreate(CreateView):
    model = Device
    form_class = DeviceForm


class DeviceUpdate(UpdateView):
    model = Device
    form_class = DeviceForm


class DeviceDelete(DeleteView):
    model = Device
    success_url = reverse_lazy('property:devices')


class MaterialList(ListView):
    model = Material


class MaterialCreate(CreateView):
    model = Material
    form_class = MaterialForm


class MaterialUpdate(UpdateView):
    model = Material
    form_class = MaterialForm


class MaterialDelete(DeleteView):
    model = Material
    success_url = reverse_lazy('property:Materials')
