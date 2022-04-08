import re
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def login_page(request):
    return render(request,'Account/pages-login.html',{})

def register_view(request):
    if request.method == 'POST':
        firstname=request.POST['first_name']
    return render(request,'Account/pages-register.html',{})