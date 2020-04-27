from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from config.settings import ITEMS_PER_PAGE

from asset.forms import DeviceForm
from stock.models import DeviceOperate, MaterialIn, Application, ApplicationDetail
from stock.forms import DeviceOperateForm, MaterialInForm, ApplicationForm, ApplicationDetailForm


class DeviceOperateList(ListView):
    model = DeviceOperate
    paginate_by = ITEMS_PER_PAGE

    def get_queryset(self):
        if self.kwargs["operate"] == 1 or self.kwargs["operate"] == 2:
            return DeviceOperate.objects.filter(operate=self.kwargs["operate"])
        else:            
            return DeviceOperate.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DeviceOperateList, self).get_context_data(**kwargs)
        context['theurl'] = reverse_lazy("basic:wordbooks")
        context['operate']=self.kwargs["operate"]
        return context    

class DeviceOperateCreate(CreateView):
    model = DeviceOperate
    form_class = DeviceOperateForm

    def get_context_data(self, **kwargs):
        context = super(DeviceOperateCreate, self).get_context_data(**kwargs)
        #处理数据库记录对应的表单
        if self.request.method == 'POST':
            deviceForm = DeviceForm(self.request.POST, prefix='deviceForm')
        else:
            deviceForm = DeviceForm(prefix='deviceForm')
        #注意要把自己处理的表单放到context上下文中，供模板文件使用
        context['deviceForm'] = deviceForm
        context['operate'] = self.kwargs["operate"]
        context['new']=1
        return context

    def form_valid(self, form):
	    #DeviceOperate不能保存，因为对应的device还未保存，所以commit传为False
        deviceop = form.save(commit=False)
		#获取上面get_context_data方法中在POST里得到的表单
        context = self.get_context_data()		
        device = context['deviceForm'].save()
        deviceop.device = device
        if self.kwargs["operate"] == 1 or self.kwargs["operate"] == 2:
            deviceop.operate = self.kwargs["operate"]
        else:
            deviceop.operate = 0
        deviceop.save()
        
        return super(DeviceOperateCreate, self).form_valid(form)


class DeviceOperateUpdate(UpdateView):
    model = DeviceOperate
    form_class = DeviceOperateForm

    def get_context_data(self, **kwargs):
        context = super(DeviceOperateCreate, self).get_context_data(**kwargs)
        #处理数据库记录对应的表单
        if self.request.method == 'POST':
            deviceForm = DeviceForm(self.request.POST, prefix='deviceForm')
        else:
            deviceForm = DeviceForm(prefix='deviceForm')
        #注意要把自己处理的表单放到context上下文中，供模板文件使用
        context['deviceForm'] = deviceForm
        return context

    def form_valid(self, form):
	    #DeviceOperate不能保存，因为对应的device还未保存，所以commit传为False
        DeviceOperate = form.save(commit=False)
		#获取上面get_context_data方法中在POST里得到的表单
        context = self.get_context_data()		
        device = context['deviceForm'].save()
        DeviceOperate.device=device
        DeviceOperate.save()
        
        return super(DeviceOperateCreate, self).form_valid(form)


class DeviceOperateDelete(DeleteView):
    model = DeviceOperate
    success_url = reverse_lazy('stock:DeviceOperates')


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


class ApplicationList(ListView):
    model = Application


class ApplicationCreate(CreateView):
    model = Application
    form_class = ApplicationForm

    def get_context_data(self, **kwargs):
        context = super(ApplicationCreate, self).get_context_data(**kwargs)
        #处理数据库记录对应的表单
        details={}
        if self.request.method == 'POST':
            for i in range(10):
                details[i] = ApplicationDetailForm(self.request.POST, prefix='detailForm'+str(i))
        else:
            for i in range(10):
                details[i] = ApplicationDetailForm(prefix='detailForm'+str(i))
        #注意要把自己处理的表单放到context上下文中，供模板文件使用
        for i in range(10):
            context['detailForm'+str(i)] = details[i]
        return context

    def form_valid(self, form):
	    #保存Application
        application = form.save()
		#获取上面get_context_data方法中在POST里得到的表单
        context = self.get_context_data()
        for i in range(10):	
            detail = context['detailForm' + str(i)].save(commit=False)
            detail.application = application
            detail.save()
                
        return super(ApplicationCreate, self).form_valid(form)


class ApplicationUpdate(UpdateView):
    model = Application
    form_class = ApplicationForm

    def get_context_data(self, **kwargs):
        context = super(ApplicationUpdate, self).get_context_data(**kwargs)
        #处理数据库记录对应的表单
        details={}
        if self.request.method == 'POST':
            for i in range(10):
                details[i] = ApplicationDetailForm(self.request.POST, prefix='detailForm'+str(i))
        else:
            for i in range(10):
                details[i] = ApplicationDetailForm(prefix='detailForm'+str(i))
        #注意要把自己处理的表单放到context上下文中，供模板文件使用
        for i in range(10):
            context['detailForm'+str(i)] = details[i]
        return context

    def form_valid(self, form):
	    #保存Application
        application = form.save()
		#获取上面get_context_data方法中在POST里得到的表单
        context = self.get_context_data()
        for i in range(10):	
            detail = context['detailForm' + str(i)].save(commit=False)
            detail.application = application
            detail.save()
                
        return super(ApplicationUpdate, self).form_valid(form)


class ApplicationDelete(DeleteView):
    model = Application
    success_url = reverse_lazy('stock:Applications')


