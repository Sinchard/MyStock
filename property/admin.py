from django.contrib import admin

from property.models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'sn', 'classification', 'model', 'value', 'asset', 'sap', 'status', 'warehouse', 'location', 'create_date', 'modify_date',
                    'description', 'attach')
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-modify_date', )
    # 后台数据列表排序方式
    list_display_links = ('id', )
    # 设置哪些字段可以点击进入编辑界面
