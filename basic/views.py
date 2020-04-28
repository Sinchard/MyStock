from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from dal import autocomplete

from config.settings import ITEMS_PER_PAGE

from basic.models import Wordbook, Category, Warehouse
from basic.forms import WordbookForm, CategoryForm, WarehouseForm


class CategoryList(ListView):
    model = Category


class CategoryCreate(CreateView):
    model = Category
    fields = ['name', 'description']


class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name', 'description']


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('categories')


class WordbookList(ListView):
    model = Wordbook
    paginate_by = ITEMS_PER_PAGE

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WordbookList, self).get_context_data(**kwargs)
        context['theurl'] = reverse_lazy("basic:wordbooks")
        return context    


class WordbookCreate(CreateView):
    model = Wordbook
    form_class = WordbookForm


class WordbookUpdate(UpdateView):
    model = Wordbook
    form_class = WordbookForm


class WordbookDelete(DeleteView):
    model = Wordbook
    success_url = reverse_lazy('wordbooks')

class WordbookAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Country.objects.none()

        qs = Wordbook.objects.all()

        if self.q:
            qs = qs.filter(sn__icontains=self.q)

        return qs

class WarehouseList(ListView):
    model = Warehouse
    paginate_by = ITEMS_PER_PAGE


class WarehouseCreate(CreateView):
    model = Warehouse
    form_class = WarehouseForm


class WarehouseUpdate(UpdateView):
    model = Warehouse
    form_class = WarehouseForm


class WarehouseDelete(DeleteView):
    model = Warehouse
    success_url = reverse_lazy('Warehouses')
