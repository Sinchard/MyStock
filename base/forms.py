from django.forms import ModelForm

from basic.models import Category, Wordbook


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ['check', 'create_date', 'modify_date']


class WordbookForm(ModelForm):
    class Meta:
        model = Wordbook
        exclude = ['check', 'create_date', 'modify_date']