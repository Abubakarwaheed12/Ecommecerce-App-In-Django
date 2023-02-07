from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from accounts.helpers import send_forget_password_mail
from accounts.models import Profile
# below library for generating random strings
import uuid
# Create your views here.

# Login

def loginuser(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('pass1')
        print(uname , pass1)
        user1=authenticate(request,username=uname,password=pass1)
        print(user1)
        if user1 is not None:
            login(request, user1)
            messages.success(request, 'login Successfullty')
            return redirect('cart')
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
                User.objects.create_user(username=uname , email=email , password=pass1)
                messages.success(request, 'your account has been created successfully')

    return render(request, 'customerregistration.html')


# Logout

def logoutuser(request):
    logout(request)
    return redirect('/')



def ChangePassword(request , token):
    context={}
    try:
        profile_obj=Profile.objects.get(forget_password_token=token)
        print(profile_obj)
        context={'user_id':profile_obj.user.id}
        if request.method=='POST':
            id=request.POST.get('u_id')
            pass1=request.POST.get('pass1')
            pass2=request.POST.get('pass2')
            print(id , pass1 , pass2)      
            if id is None:
                  messages.warning(request, 'no user found')
                  return redirect(f'resest_password/{token}')
            if pass1 !=pass2:
                messages.warning(request, 'both passwords should be same ')
                return redirect(f'resest_password/{token}')
            userobj=User.objects.get(id=id)
            userobj.set_password(pass1)
            userobj.save()
            messages.success(request, 'your password has been updated successfully now you can login')
                        
    except Exception as e :
        print(e)
    return render(request, 'reset_password.html' , context=context)


def ForgetPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            
            if not User.objects.filter(username=username).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('forgotPassword')
            
            user_obj = User.objects.get(username = username)
            mail=user_obj.email
            token = str(uuid.uuid4())
            profile_obj= Profile.objects.get(user = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email , token)
            messages.success(request, f'An email is sent to your email address {mail}.')
            return redirect('forgotPassword')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'forgot.html')