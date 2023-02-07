from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import AllProducts , Cart
# Home View
def home(request):
    products=AllProducts.objects.all()[:4]
    context={
        'products':products,
    }
    return render(request, 'app/home.html' , context)



# product_listing View
def product_listing(request):
    products=AllProducts.objects.all()[:4]
    context={
        'products':products,
    }
    return render(request, 'app/productlist.html' , context)
 
# Product Detail Page 
def product_detail(request , id):
    product=AllProducts.objects.get(pk=id)
    context={
        'product':product,
    }
    return render(request, 'app/productdetail.html' , context)


#  Add to Cart View
@login_required(login_url='login')
def add_to_cart(request):
    user=request.user
    prod_id=request.GET.get('product_id')
    prod=AllProducts.objects.get(id=prod_id)
    print(prod)
    # print(f'the product id  is : {prod_id}')
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


