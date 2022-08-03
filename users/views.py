from django.shortcuts import render, redirect 
from .models import User, Pharmasist, SaleMen
from django.http import HttpResponse
import datetime
from .forms import RegisterUserForm, RegisterPharmasistForm, RegisterSaleMenForm

# Create your views here.

def user_profile(requests,pk):
    profile = User.objects.get(pk=pk) 
    
    
def user_profile_list(requests):
    profiles = Profile.objects.exclude(user=request.user) 

def create_user(request):
    name1 = User.first_name
    name2 = User.last_name
    form_user = RegisterUserForm(request.POST or None) 
    if request.method == 'POST':
        if form_user.is_valid():
            form_user.save()
            page = f"Welcome {self.name1, self.name2} to Pharmastore" 
            
            

def delete_user(request):
    pass 


def update_user(request):
    pass  


def create_pharmasist(request):
    form_pharm = RegisterPharmasistForm(request.POST or None) 
    if request.method == 'POST':
        if form_pharm.is_valid():
            form_pharm.save() 


def update_pharmasist(request):
    pass 


def delete_pharmasist(request):
    pass


def create_salemen(request):
    form_sm = RegisterSaleMenForm(request.POST or None) 
    if request.method == 'POST':
        if form_sm.is_valid():
            form_sm.save()


def update_salemen(request):
    pass 


def delete_salemen(request):
    pass


def date_year(request):
    current_date = datetime.date.today("Y")  
    html = "<html><body><b>Current Date and Time Value:</b> %s</body></html>" % current_date
    return HttpResponse(html)