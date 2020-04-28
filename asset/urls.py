from django.urls import path
from asset.views import DeviceAutocomplete
from asset.views import DeviceList, DeviceCreate, DeviceUpdate, DeviceDelete
from asset.views import MaterialList, MaterialCreate, MaterialUpdate, MaterialDelete

app_name = 'asset'

urlpatterns = [
     path('device-autocomplete/', DeviceAutocomplete.as_view(), name='device-autocomplete'),
    path('devices', DeviceList.as_view(), name='devices'),
    path('device/add', DeviceCreate.as_view(), name='add_device'),
    path('device/<int:pk>/', DeviceUpdate.as_view(), name='edit_device'),
    path('device/<int:pk>/delete', DeviceDelete.as_view(), name='delete_device'),
    path('materials', MaterialList.as_view(), name='materials'),
    path('material/add', MaterialCreate.as_view(), name='add_material'),
    path('material/<int:pk>/', MaterialUpdate.as_view(), name='edit_material'),
    path('material/<int:pk>/delete', MaterialDelete.as_view(), name='delete_material'),
]
