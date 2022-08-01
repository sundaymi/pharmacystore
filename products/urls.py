from django.urls import path, include
from .views import product 

# app_name 

urlpatterns = [
    path(''),
    path('product/<str:d_name>', product(requests), name='product'),
    
]
