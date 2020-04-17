from django.urls import path
from base.views import CategoryList, CategoryCreate, CategoryUpdate, CategoryDelete

app_name = 'base'

urlpatterns = [
    path('categories', CategoryList.as_view(), name='categories'),
    path('category/add', CategoryCreate.as_view(), name='add_category'),
    path('category/<int:pk>/', CategoryUpdate.as_view(), name='edit_category'),
    path('category/<int:pk>/delete',
         CategoryDelete.as_view(),
         name='delete_category'),
]