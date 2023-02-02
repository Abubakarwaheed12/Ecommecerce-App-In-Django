from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
# Create your views here.

def loginuser(request):
 return render(request, 'login.html')

def customerregistration(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass1')
        if pass1 != pass2 :
            messages.warning(request, 'your password does not match')
        else:
            user=User(username=uname , email=email , password=pass1)
            user.save()
            messages.success(request, 'your account has been created successfully')

    return render(request, 'customerregistration.html')