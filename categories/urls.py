from django.urls import path, include 
from .views import category

# app_name = pharmastore

urlpatterns = [
    path(''),
    path('category/<str:c_name>', category(request), name='category'),
    
]
