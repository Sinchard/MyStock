from django.shortcuts import render
from django.http import HttpResponse

from stock.models import Warehouse
	
def index(request):
    return HttpResponse("Rango says hey there partner!")

def show_warehouse(request):
    warehouses = Warehouse.objects.all()
    context_dict = {"title": "库房列表 -- 库存管理系统"}
    context_dict["warehouses"]=warehouses
    return render(request, 'stock/warehouse.html', context_dict)