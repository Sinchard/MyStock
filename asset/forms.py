from django.forms import ModelForm

from asset.models import Device, Material


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        exclude = []


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        exclude = []
