from django.urls import path
from basic.views import CategoryList, CategoryCreate, CategoryUpdate, CategoryDelete
from basic.views import WordbookList, WordbookCreate, WordbookUpdate, WordbookDelete, WordbookAutocomplete
from basic.views import WarehouseList, WarehouseCreate, WarehouseUpdate, WarehouseDelete

app_name = 'basic'

urlpatterns = [
    path('categories', CategoryList.as_view(), name='categories'),
    path('category/add', CategoryCreate.as_view(), name='add_category'),
    path('category/<int:pk>/', CategoryUpdate.as_view(), name='edit_category'),
    path('category/<int:pk>/delete',
         CategoryDelete.as_view(),
         name='delete_category'),
    path('wordbooks', WordbookList.as_view(), name='wordbooks'),
    path('wordbook/add', WordbookCreate.as_view(), name='add_wordbook'),
    path('wordbook/<int:pk>/', WordbookUpdate.as_view(), name='edit_wordbook'),
    path('wordbook/<int:pk>/delete',
         WordbookDelete.as_view(),
         name='delete_wordbook'),
     path('wordbook-autocomplete/', WordbookAutocomplete.as_view(), name='wordbook-autocomplete'),
    path('warehouses', WarehouseList.as_view(), name='warehouses'),
    path('warehouse/add', WarehouseCreate.as_view(), name='add_warehouse'),
    path('warehouse/<int:pk>/', WarehouseUpdate.as_view(), name='edit_warehouse'),
    path('warehouse/<int:pk>/delete',
         WarehouseDelete.as_view(),
         name='delete_warehouse'),
]
