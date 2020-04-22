from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from asset.forms import DeviceForm
from stock.models import DeviceIn, MaterialIn
from stock.forms import DeviceInForm, MaterialInForm


class DeviceInList(ListView):
    model = DeviceIn


class DeviceInCreate(CreateView):
    model = DeviceIn
    form_class = DeviceInForm

    def get_context_data(self, **kwargs):
        context = super(DeviceInCreate, self).get_context_data(**kwargs)
        #处理数据库记录对应的表单
        if self.request.method == 'POST':
            deviceForm = DeviceForm(self.request.POST, prefix='deviceForm')
        else:
            deviceForm = DeviceForm(prefix='deviceForm')
        #注意要把自己处理的表单放到context上下文中，供模板文件使用
        context['deviceForm'] = deviceForm
        return context

    def form_valid(self, form):
	    #DeviceIn不能保存，因为对应的device还未保存，所以commit传为False
        devicein = form.save(commit=False)
		#获取上面get_context_data方法中在POST里得到的表单
        context = self.get_context_data()		
        device = context['deviceForm'].save()
        devicein.device=device
        devicein.save()
        
        return super(DeviceInCreate, self).form_valid(form)


class DeviceInUpdate(UpdateView):
    model = DeviceIn
    form_class = DeviceInForm


class DeviceInDelete(DeleteView):
    model = DeviceIn
    success_url = reverse_lazy('stock:deviceins')


class MaterialInList(ListView):
    model = MaterialIn


class MaterialInCreate(CreateView):
    model = MaterialIn
    form_class = MaterialInForm


class MaterialInUpdate(UpdateView):
    model = MaterialIn
    form_class = MaterialInForm


class MaterialInDelete(DeleteView):
    model = MaterialIn
    success_url = reverse_lazy('stock:materialins')


