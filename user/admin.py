from django.contrib import admin

from user.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'department', 'team', 'phone',
                    'mobile', 'modify_date')
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-modify_date', )
    # 后台数据列表排序方式
    list_display_links = ('id', 'name')
    # 设置哪些字段可以点击进入编辑界面
