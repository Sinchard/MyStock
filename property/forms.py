from django.forms import ModelForm

from property.models import Device


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        exclude = []
