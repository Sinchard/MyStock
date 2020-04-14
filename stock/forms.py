import datetime

from django import forms
from django.forms import TextInput, Textarea, Select

from stock.models import Warehouse


class WarehouseForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': '2'
    }),
                                  required=False)

    class Meta:
        model = Warehouse
        fields = ('id', 'name', 'location', 'description')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'location': TextInput(attrs={'class': 'form-control'}),
        }