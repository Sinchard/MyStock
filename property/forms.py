from django.forms import ModelForm

from property.models import Device, Material


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        exclude = []


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        exclude = []
