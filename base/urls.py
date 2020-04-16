from django.urls import path
from base import views

app_name = 'base'

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.show_wordbook, name='wordbooks'),
    path('add', views.add_wordbook, name='add_wordbook'),
]