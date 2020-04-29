import datetime

from django import forms
from django.forms import TextInput, Textarea, Select

from dal import autocomplete

from asset.models import Device
from stock.models import DeviceOperate, MaterialIn, Application, ApplicationDetail
from django.forms.models import inlineformset_factory

class DeviceOperateForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}), required=False)

    class Meta:
        model = DeviceOperate
        fields = ['id', 'device', 'warehouse', 'employee', 'description']
        widgets = {
            'device': autocomplete.ModelSelect2(
                            url='asset:device-autocomplete',
                            attrs={'class': 'form-control'}
                        ),
            'warehouse': Select(attrs={'class': 'form-control'}),
            'employee': autocomplete.ModelSelect2(
                            url='user:employee-autocomplete',
                            attrs={'class': 'form-control'}
                        ),
        }    

class MaterialInForm(forms.ModelForm):
    class Meta:
        model = MaterialIn
        exclude = ['check', 'create_date', 'modify_date']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['id', 'name', 'applicant', 'status', 'approver', 'approve_content', 'approve_date',
                    'confirmed', 'confirm_content', 'confirm_date', 'description']

DetailFormSet = inlineformset_factory(Application, ApplicationDetail, fields=('name', 'number', 'location', 'is_device', 'description'),
                                          extra=10, can_delete=False, max_num=15)
class ApplicationDetailForm(forms.ModelForm):
    class Meta:
        model = ApplicationDetail
        fields = ['name', 'number', 'location', 'is_device', 'description']                    