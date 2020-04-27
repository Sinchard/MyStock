from django.urls import path
from stock.views import DeviceOperateList, DeviceOperateCreate, DeviceOperateUpdate, DeviceOperateDelete
from stock.views import ApplicationList, ApplicationCreate, ApplicationUpdate, ApplicationDelete

app_name = 'stock'

urlpatterns = [
    path('DeviceOperates', DeviceOperateList.as_view(), name='DeviceOperates'),
    path('DeviceOperate/add', DeviceOperateCreate.as_view(), name='add_DeviceOperate'),
    path('DeviceOperate/<int:pk>/', DeviceOperateUpdate.as_view(), name='edit_DeviceOperate'),
    path('DeviceOperate/<int:pk>/delete', DeviceOperateDelete.as_view(), name='delete_DeviceOperate'),

    path('applications', ApplicationList.as_view(), name='applications'),
    path('application/add', ApplicationCreate.as_view(), name='add_application'),
    path('application/<int:pk>/', ApplicationUpdate.as_view(), name='edit_application'),
    path('application/<int:pk>/delete', ApplicationDelete.as_view(), name='delete_application'),
]