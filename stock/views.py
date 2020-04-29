from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from config.settings import ITEMS_PER_PAGE

from asset.forms import DeviceForm
from stock.models import DeviceOperate, MaterialIn, Application, ApplicationDetail
from stock.forms import ApplicationDetailForm, ApplicationForm, DetailFormSet, DeviceOperateForm, MaterialInForm
from django.http import HttpResponseRedirect


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
        context['theurl'] = reverse_lazy("stock:deviceins")
        context['operate']=self.kwargs["operate"]
        return context    

class DeviceOperateCreate(CreateView):
    model = DeviceOperate
    form_class = DeviceOperateForm

    def get_context_data(self, **kwargs):
        context = super(DeviceOperateCreate, self).get_context_data(**kwargs)
        context['operate'] = self.kwargs["operate"]
        context['new']=1
        return context

    def form_valid(self, form):
        deviceop = form.save(commit=False)
        deviceop.location = ""
        if self.kwargs["operate"] == 1 or self.kwargs["operate"] == 2:
            deviceop.operate = self.kwargs["operate"]
        else:
            deviceop.operate = 0
        deviceop.save()
        
        return super(DeviceOperateCreate, self).form_valid(form)


class DeviceOperateUpdate(UpdateView):
    model = DeviceOperate
    form_class = DeviceOperateForm



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

set_data = {'form-TOTAL_FORMS': '10', 'form-INITIAL_FORMS': '10', 'form-MAX_NUM_FORMS': '10' }

class ApplicationCreate(CreateView):
    model = Application
    form_class = ApplicationForm

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detailSets = DetailFormSet()
        return self.render_to_response(self.get_context_data(form=form, detailSets=detailSets))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detailSets = DetailFormSet(self.request.POST)
        if (form.is_valid() and detailSets.is_valid()):
            return self.form_valid(form, detailSets)
        else:
            return self.form_invalid(form, detailSets)

    def form_valid(self, form, detailSets):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        detailSets.instance = self.object
        detailSets.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, detailSets):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, detailSets=detailSets))


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


