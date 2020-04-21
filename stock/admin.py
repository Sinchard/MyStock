from django.contrib import admin

from stock.models import DeviceIn, MaterialIn


@admin.register(DeviceIn)
class DeviceInAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'warehouse', 'employee', 'check', 'create_date',
                    'modify_date', 'description', 'attach')
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-modify_date', )
    # 后台数据列表排序方式
    list_display_links = ('id', 'device')
    # 设置哪些字段可以点击进入编辑界面


@admin.register(MaterialIn)
class MaterialInAdmin(admin.ModelAdmin):
    list_display = ('id', 'material', 'amount', 'warehouse', 'employee', 'check', 'create_date',
                    'modify_date', 'description', 'attach')
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-modify_date', )
    # 后台数据列表排序方式
    list_display_links = ('id', 'material')
    # 设置哪些字段可以点击进入编辑界面
