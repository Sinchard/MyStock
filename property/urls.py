from django.urls import path
from property.views import DeviceList, DeviceCreate, DeviceUpdate, DeviceDelete

app_name = 'property'

urlpatterns = [
    path('devices', DeviceList.as_view(), name='devices'),
    path('device/add', DeviceCreate.as_view(), name='add_device'),
    path('device/<int:pk>/', DeviceUpdate.as_view(), name='edit_device'),
    path('device/<int:pk>/delete',
         DeviceDelete.as_view(),
         name='delete_device'),
]
