import datetime

from django import forms
from django.forms import TextInput, Textarea, Select

from stock.models import DeviceIn, MaterialIn


class DeviceInForm(forms.ModelForm):
    
    class Meta:
        model = DeviceIn
        fields = ['employee', 'warehouse', 'description']
        #exclude = ['device','check', 'create_date', 'modify_date']
    

class MaterialInForm(forms.ModelForm):
    class Meta:
        model = MaterialIn
        exclude = ['check', 'create_date', 'modify_date']