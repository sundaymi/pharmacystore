from django.urls import path, include 
from .views import user_profile, user_profile_list, create_user, update_user, delete_user

# app_name = pharmastore 

urlpatterns = [
    path(''),
    path('user_profile', user_profile(requests, pk),name='user_profile'),
    path('user_profile_list', user_profile_list(requests),name='user_profile_list'),
    path('create_user',create_user(request),name='create_user'),
    path('update_user',update_user(request),name='update_user'), 
    path('delete_user',delete_user(request),name='delete_user'),
    
]
