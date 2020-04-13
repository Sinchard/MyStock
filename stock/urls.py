from django.urls import path
from stock import views
	
app_name = 'stock'

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.show_warehouse, name='show_warehouse'),
]