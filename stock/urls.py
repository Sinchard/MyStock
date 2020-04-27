from django.urls import path
from stock.views import DeviceOperateList, DeviceOperateCreate, DeviceOperateUpdate, DeviceOperateDelete
from stock.views import ApplicationList, ApplicationCreate, ApplicationUpdate, ApplicationDelete

app_name = 'stock'

urlpatterns = [
    # display all device in and out records
    path('deviceoperates', DeviceOperateList.as_view(), name='deviceoperates'),
    path('deviceoperate/<int:pk>/delete', DeviceOperateDelete.as_view(), name='delete_deviceoperate'),
    # device in operate
    path('deviceins', DeviceOperateList.as_view(), {'operate': 1}, name='deviceins'),
    path('devicein/add', DeviceOperateCreate.as_view(), {'operate': 1}, name='add_devicein'),
    path('devicein/<int:pk>/', DeviceOperateUpdate.as_view(), {'operate': 1}, name='edit_devicein'),
    # device out operate
    path('deviceouts', DeviceOperateList.as_view(), {'operate': 2}, name='deviceouts'),
    path('deviceout/add', DeviceOperateCreate.as_view(), {'operate': 2}, name='add_deviceout'),
    path('deviceout/<int:pk>/', DeviceOperateUpdate.as_view(), {'operate': 2}, name='edit_deviceout'),

    path('applications', ApplicationList.as_view(), name='applications'),
    path('application/add', ApplicationCreate.as_view(), name='add_application'),
    path('application/<int:pk>/', ApplicationUpdate.as_view(), name='edit_application'),
    path('application/<int:pk>/delete', ApplicationDelete.as_view(), name='delete_application'),
]