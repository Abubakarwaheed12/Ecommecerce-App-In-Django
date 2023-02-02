from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from accounts.helpers import send_fogot_password_mail
# below library for generating random strings
import uuid
# Create your views here.

# Login

def loginuser(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('pass1')
        print(uname , pass1)
        user=authenticate(request, username=uname , password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, 'login Successfullty')
            return redirect('add-to-cart')
        else:
            messages.warning(request, 'please enter correct information')
    return render(request, 'login.html')

# Register

def customerregistration(request):
    if request.user.is_anonymous:
        if request.method=='POST':
            uname=request.POST.get('username')
            email=request.POST.get('email')
            pass1=request.POST.get('pass1')
            pass2=request.POST.get('pass1')
            eunmae=User.objects.filter(username=uname)
            if eunmae:
                messages.warning(request, 'Username already exist')
            if pass1 != pass2 :
                messages.warning(request, 'your password does not match Now You Can Login')
            else:
                user=User(username=uname , email=email , password=pass1)
                user.save()
                messages.success(request, 'your account has been created successfully')

    return render(request, 'customerregistration.html')


# Forgot Password
def forgotPassword(request):
    try:
        if request.method=='POST':
            uname=request.POST.get('username')
            # print(uname)
            if not User.objects.filter(username=uname).first():
                messages.warning(request, 'user not Found')
                return redirect('forgotPassword')

            user_obj=User.objects.get(username=uname)
            # email=user_obj.objects.get(email)
            token=str(uuid.uuid4())
            send_fogot_password_mail(user_obj, token)
            messages.success(request, 'email sent')
            return redirect('forgotPassword')
            
    except Exception as e:
        print(e)
    return render(request, 'forgot.html')
    
# Reset Password
def reset_password(request):
    return render(request, 'reset_password.html')
# Logout

def logoutuser(request):
    logout(request)
    return redirect('/')