from django import forms
from .models import User, SaleMen, Pharmasist

class RegisterUserForm(forms.Form):
    
    username = forms.Charfield(label="Username",max_length=100) 
    password =  forms.CharField(label="Password",widget=forms.PasswordInput(), validators=[validators.MinLengthValidator(8)])
    confirm_password = forms.CharField(label="Confirm password",widget=forms.PasswordInput())
    firstname = forms.Charfield(label="First name",max_length=100) 
    lastname = forms.Charfield(label="Last name",max_length=120)  
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='Phone',required=False)
    
    
class RegisterPharmasistForm(forms.Form):
    username = forms.Charfield(max_length=100) 
    password =  forms.CharField(widget=forms.PasswordInput(), validators=[validators.MinLengthValidator(8)])
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    firstname = forms.Charfield(max_length=100) 
    lastname = forms.Charfield(max_length=120)  
    email = forms.EmailField()
    phone_number = forms.CharField(label='Phone',required=False)
    

class RegisterSaleMenForm(forms.Form):
    username = forms.Charfield(max_length=100) 
    password =  forms.CharField(widget=forms.PasswordInput(), validators=[validators.MinLengthValidator(8)])
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    firstname = forms.Charfield(max_length=100) 
    lastname = forms.Charfield(max_length=120)  
    email = forms.EmailField()
    phone_number = forms.CharField(label='Phone',required=False)


class LoginForm(forms.Form):
    email_login = forms.EmailField()
    password_login = forms.CharField(widget=forms.PasswordInput())
    

class UpdateUserForm(forms.Form):
    pass 


class DeleteUserForm(forms.Form): 
    pass 


class UpdatePharmasistForm(forms.Form):
    pass 


class DeletPharmasistForm(forms.Form):
    pass 


class UpdateSalemenForm(forms.Form):
    pass 


class DeleteSalemenForm(forms.Form):
    pass 

