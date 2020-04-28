from django import forms
from django.forms import TextInput, Textarea, Select

from dal import autocomplete

from asset.models import Device, Material


class DeviceForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    value = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False, initial=0)
    asset = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    sap = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}), required=False)
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Device
        fields = ('id', 'classification', 'brand', 'model', 'sn', 'value', 'asset', 'sap', 'good','description')
        widgets = {
            'classification': autocomplete.ModelSelect2(
                        url='basic:wordbook-autocomplete',
                        attrs={'class': 'form-control'}
                    ),
            'brand': autocomplete.ModelSelect2(
                        url='basic:wordbook-autocomplete',
                        attrs={'class': 'form-control'},
                        forward=['type'],
                    ),
            'model': autocomplete.ModelSelect2(
                        url='basic:wordbook-autocomplete',
                        attrs={'class': 'form-control'},
                        forward=['name'],
                    ),
            'sn': TextInput(attrs={'class': 'form-control'}),
            'good': Select(attrs={'class': 'form-control'}),
        }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        exclude = []
