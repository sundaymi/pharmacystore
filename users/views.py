from django.shortcuts import render
from .models import User
from django.http import HttpResponse
import datetime

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


def date_year(request):
    current_date = datetime.date.today("Y")  
    html = "<html><body><b>Current Date and Time Value:</b> %s</body></html>" % current_date
    return HttpResponse(html)