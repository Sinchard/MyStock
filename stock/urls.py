from django.urls import path
from stock.views import DeviceInList, DeviceInCreate, DeviceInUpdate, DeviceInDelete
from stock.views import ApplicationList, ApplicationCreate, ApplicationUpdate, ApplicationDelete

app_name = 'stock'

urlpatterns = [
    path('deviceins', DeviceInList.as_view(), name='deviceins'),
    path('devicein/add', DeviceInCreate.as_view(), name='add_devicein'),
    path('devicein/<int:pk>/', DeviceInUpdate.as_view(), name='edit_devicein'),
    path('devicein/<int:pk>/delete', DeviceInDelete.as_view(), name='delete_devicein'),

    path('applications', ApplicationList.as_view(), name='applications'),
    path('application/add', ApplicationCreate.as_view(), name='add_application'),
    path('application/<int:pk>/', ApplicationUpdate.as_view(), name='edit_application'),
    path('application/<int:pk>/delete', ApplicationDelete.as_view(), name='delete_application'),
]