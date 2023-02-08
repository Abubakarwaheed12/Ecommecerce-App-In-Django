from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import AllProducts , Cart
from django.db.models import Q
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
    Cart(user=user , Item=prod).save()
    print(prod)
    return redirect('cart')

#  Show Cart 
@login_required(login_url='login')
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0.00
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        if cart_product:
            for p in cart_product:
                temp_amount=(p.Quantity*p.Item.price)
                amount +=temp_amount
                total_amount=amount+shipping_amount
                print(temp_amount)
            context={
                'carts':cart,
                'tempamount':temp_amount,
                'amount':amount,
                'total_amount':total_amount,
            }
            return render(request, 'app/addtocart.html' , context)
        else:
            return render(request, 'app/emptycart.html')

# Plus 
def cart_plus(request):
    if request.method=='GET':
        id=request.GET['prod_id']
        c=Cart.objects.get(Q(Item=id) & Q(user=request.user))
        print(c)
        c.Quantity =2
        c.save()
        print(cart)
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


