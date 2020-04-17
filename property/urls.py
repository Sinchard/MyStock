from django.urls import path
from base import views

app_name = 'property'

urlpatterns = [
    #path('', views.index, name='index'),
    path('wordbooks', views.show_wordbook, name='wordbooks'),
    path('wordbooks/add', views.add_wordbook, name='add_wordbook'),
    path('categories', views.CategoryList.as_view(), name='categories'),
]