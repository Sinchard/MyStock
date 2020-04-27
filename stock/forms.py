import datetime

from django import forms
from django.forms import TextInput, Textarea, Select

from stock.models import DeviceOperate, MaterialIn, Application, ApplicationDetail


class DeviceOperateForm(forms.ModelForm):
    
    class Meta:
        model = DeviceOperate
        fields = ['id', 'device','employee', 'warehouse', 'description']
        #exclude = ['device','check', 'create_date', 'modify_date']
    

class MaterialInForm(forms.ModelForm):
    class Meta:
        model = MaterialIn
        exclude = ['check', 'create_date', 'modify_date']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['id', 'name', 'applicant', 'status', 'approver', 'approve_content', 'approve_date',
                    'confirmed', 'confirm_content', 'confirm_date', 'description']
                    
class ApplicationDetailForm(forms.ModelForm):
    class Meta:
        model = ApplicationDetail
        fields = ['name', 'number', 'location', 'is_device']                    