from django.urls import path
from basic.views import CategoryList, CategoryCreate, CategoryUpdate, CategoryDelete

from user.views import UserProfileList, UserProfileCreate, UserProfileUpdate, UserProfileDelete, UserProfileAutocomplete

app_name = 'user'

urlpatterns = [
    path('profiles', UserProfileList.as_view(), name='profiles'),
    path('profile/add', UserProfileCreate.as_view(), name='add_profile'),
    path('profile/<int:pk>/', UserProfileUpdate.as_view(),
         name='edit_profile'),
    path('profile/<int:pk>/delete',
         UserProfileDelete.as_view(),
         name='delete_profile'),
path('employee-autocomplete/', UserProfileAutocomplete.as_view(), name='employee-autocomplete'),
]
