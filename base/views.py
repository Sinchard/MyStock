from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from base.models import Wordbook, Category
from base.forms import WordbookForm, CategoryForm


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


class WordbookCreate(CreateView):
    model = Wordbook
    form_class = WordbookForm


class WordbookUpdate(UpdateView):
    model = Wordbook
    form_class = WordbookForm


class WordbookDelete(DeleteView):
    model = Wordbook
    success_url = reverse_lazy('wordbooks')

