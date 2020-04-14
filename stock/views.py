from django.shortcuts import render, redirect
from django.http import HttpResponse

from stock.models import Warehouse
from stock.forms import WarehouseForm


def index(request):
    return HttpResponse("Rango says hey there partner!")


def show_warehouse(request):
    warehouses = Warehouse.objects.all()
    context_dict = {"title": "库房列表 -- 库存管理系统"}
    context_dict["warehouses"] = warehouses
    return render(request, 'stock/warehouse.html', context_dict)


def add_warehouse(request):
    form = WarehouseForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = WarehouseForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved, we could confirm this.
            # For now, just redirect the user back to the index view.
            return redirect('/stock/')
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)

    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'stock/add_warehouse.html', {'form': form})
