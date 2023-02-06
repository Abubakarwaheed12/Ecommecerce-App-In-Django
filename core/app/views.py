from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Home View
def home(request):
 return render(request, 'app/home.html')




# product_listing View
def product_listing(request):
    return render(request, 'app/productlist.html')


def add_to_cart(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'login first to access the Cart Page')
        return redirect('login')
    return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def checkout(request):
 return render(request, 'app/checkout.html')


def product_detail(request):
 return render(request, 'app/productdetail.html')