from django.contrib import admin

from basic.models import Category, Wordbook, CategoryShip


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'check', 'create_date', 'modify_date',
                    'description', 'attach')
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-modify_date', )
    #后台数据列表排序方式
    list_display_links = ('id', 'name')
    # 设置哪些字段可以点击进入编辑界面


@admin.register(Wordbook)
class WordbookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'check', 'create_date',
                    'modify_date', 'description', 'attach')
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-modify_date', )
    #后台数据列表排序方式
    list_display_links = ('id', 'name')
    # 设置哪些字段可以点击进入编辑界面


@admin.register(CategoryShip)
class CategoryShipAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'wordbook', 'create_date', 'modify_date',
                    'description', 'attach')
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-modify_date', )
    #后台数据列表排序方式
    list_display_links = ('id', )
    # 设置哪些字段可以点击进入编辑界面
