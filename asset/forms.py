from django.forms import ModelForm

from asset.models import Device, Material


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['id', 'brand', 'model', 'sn', 'classification', 'model', 'value', 'asset', 'sap', 'status',
                    'description']


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        exclude = []
