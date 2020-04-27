from django.urls import path
from stock.views import DeviceOperateList, DeviceOperateCreate, DeviceOperateUpdate, DeviceOperateDelete
from stock.views import ApplicationList, ApplicationCreate, ApplicationUpdate, ApplicationDelete

app_name = 'stock'

urlpatterns = [
    # display all device in and out records
    path('DeviceOperates', DeviceOperateList.as_view(), name='DeviceOperates'),
    path('DeviceOperate/<int:pk>/delete', DeviceOperateDelete.as_view(), name='delete_DeviceOperate'),
    # device in operate
    path('DeviceIns', DeviceOperateList.as_view(), {'operate': 1}, name='DeviceIns'),
    path('DeviceIn/add', DeviceOperateCreate.as_view(), {'operate': 1}, name='add_DeviceIn'),
    path('DeviceIn/<int:pk>/', DeviceOperateUpdate.as_view(), {'operate': 1}, name='edit_DeviceIn'),
    # device out operate
    path('DeviceOuts', DeviceOperateList.as_view(), {'operate': 2}, name='DeviceOuts'),
    path('DeviceOut/add', DeviceOperateCreate.as_view(), {'operate': 2}, name='add_DeviceOut'),
    path('DeviceOut/<int:pk>/', DeviceOperateUpdate.as_view(), {'operate': 2}, name='edit_DeviceOut'),

    path('applications', ApplicationList.as_view(), name='applications'),
    path('application/add', ApplicationCreate.as_view(), name='add_application'),
    path('application/<int:pk>/', ApplicationUpdate.as_view(), name='edit_application'),
    path('application/<int:pk>/delete', ApplicationDelete.as_view(), name='delete_application'),
]