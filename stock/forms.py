import datetime

from django import forms
from django.forms import TextInput, Textarea, Select

from stock.models import DeviceIn, MaterialIn, Application, ApplicationDetail


class DeviceInForm(forms.ModelForm):
    
    class Meta:
        model = DeviceIn
        fields = ['employee', 'warehouse', 'description']

        #exclude = ['device','check', 'create_date', 'modify_date']
    

class MaterialInForm(forms.ModelForm):
    class Meta:
        model = MaterialIn
        exclude = ['check', 'create_date', 'modify_date']


class ApplicationForm(forms.ModelForm):
    class Meta:
        module = Application
        fields = ['id', 'name', 'applicant', 'status', 'approver', 'approve_content', 'approve_date',
                    'confirmed', 'confirm_content', 'confirm_date', 'description']
                    
class ApplicationDetailForm(forms.ModelForm):
    class Meta:
        module = ApplicationDetail
        fields = ['name', 'number', 'location', 'is_device']                    