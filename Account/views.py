import email
import re
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def login_page(request):
    return render(request,'Account/pages-login.html',{})

def register_view(request):
    if request.method == 'POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        passord1=request.POST['password1']
        passord2=request.POST['password2']
    return render(request,'Account/pages-register.html',{})