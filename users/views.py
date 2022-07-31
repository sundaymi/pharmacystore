from django.shortcuts import render
from .models import User

# Create your views here.

def user_profile(requests,pk):
    profile = User.objects.get(pk=pk) 
    
def user_profile_list(requests):
    profiles = Profile.objects.exclude(user=request.user) 

def create_user(request):
    pass 

def delete_user(request):
    pass 

def update_user(request):
    pass  

