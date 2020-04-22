from django.urls import path
from stock.views import DeviceInList, DeviceInCreate, DeviceInUpdate, DeviceInDelete

app_name = 'stock'

urlpatterns = [
    path('deviceins', DeviceInList.as_view(), name='deviceins'),
    path('devicein/add', DeviceInCreate.as_view(), name='add_devicein'),
    path('devicein/<int:pk>/', DeviceInUpdate.as_view(), name='edit_devicein'),
    path('devicein/<int:pk>/delete', DeviceInDelete.as_view(), name='delete_devicein'),
]