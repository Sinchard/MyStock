from django.urls import path
from basic.views import CategoryList, CategoryCreate, CategoryUpdate, CategoryDelete
from basic.views import WordbookList, WordbookCreate, WordbookUpdate, WordbookDelete

app_name = 'basic'

urlpatterns = [
    path('categories', CategoryList.as_view(), name='categories'),
    path('category/add', CategoryCreate.as_view(), name='add_category'),
    path('category/<int:pk>/', CategoryUpdate.as_view(), name='edit_category'),
    path('category/<int:pk>/delete',
         CategoryDelete.as_view(),
         name='delete_category'),
    path('wordbooks', WordbookList.as_view(), name='wordbooks'),
    path('wordbook/add', WordbookCreate.as_view(), name='add_wordbook'),
    path('wordbook/<int:pk>/', WordbookUpdate.as_view(), name='edit_wordbook'),
    path('wordbook/<int:pk>/delete',
         WordbookDelete.as_view(),
         name='delete_wordbook'),
]