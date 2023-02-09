from django.shortcuts import render , redirect 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import AllProducts , Cart
from django.db.models import Q
from django.http import JsonResponse
# Home View
def home(request):
    total_items=0
    if request.user.is_authenticated:
        total_items=len(Cart.objects.filter(user=request.user))
        print(total_items)
    products=AllProducts.objects.all()[:4]
    context={
        'products':products,
        'total_items':total_items,
    }
    return render(request, 'app/home.html' , context)



# product_listing View
def product_listing(request):
    total_items=0
    if request.user.is_authenticated:
        total_items=len(Cart.objects.filter(user=request.user))
        print(total_items)
    products=AllProducts.objects.all()
    q=request.GET.get('q')
    print(q)
    if q:
        products=AllProducts.objects.filter(title__contains=q)
    else:
        q=''
    context={
        'products':products,
        'total_items':total_items,
    }
    return render(request, 'app/productlist.html' , context)
 
# Product Detail Page 
def product_detail(request , id):
    total_items=0
    if request.user.is_authenticated:
        total_items=len(Cart.objects.filter(user=request.user))
        print(total_items)
    product=AllProducts.objects.get(pk=id)
    context={
        'product':product,
        'total_items':total_items,
    }
    return render(request, 'app/productdetail.html' , context)


#  Add to Cart View
@login_required(login_url='login')
def add_to_cart(request):
    user=request.user
    prod_id=request.GET.get('product_id')
    prod=AllProducts.objects.get(id=prod_id)
    cart,created = Cart.objects.get_or_create(user=user , Item=prod )
    cart.save()
    prod.stock -=1
    prod.save()
    if not created:
        cart.Quantity +=1
        cart.save()
    cart.save()
    print(prod)
    return redirect('cart')

#  Show Cart 
def show_cart(request):
    total_items=0
    if request.user.is_authenticated:
        
        total_items=len(Cart.objects.filter(user=request.user))
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
                'total_items':total_items,
            }
            return render(request, 'app/addtocart.html' , context)
        else:
            total_items=0
            total_items=len(Cart.objects.filter(user=request.user))
            context={
                'total_items':total_items,
            }
            return render(request, 'app/emptycart.html' , context)

# Plus 
def cart_plus(request):
    if request.method=='GET':
        id=request.GET['prod_id']
        i=AllProducts.objects.get(id=id)
        i.stock -=1
        i.save()
        c=Cart.objects.get(Q(Item=id) & Q(user=request.user))
        c.Quantity +=1
        c.Item.price=c.Item.price*c.Quantity
        c.save()
        amount=0.00
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            temp_amount=(p.Quantity*p.Item.price)
            amount +=temp_amount
            total_amount=amount+shipping_amount
            print(temp_amount)        
            data={
                'quantity':c.Quantity,
                'amount':amount,
                'total_amount':total_amount,
                'status':200,
                'item_total_price':c.Item.price,
                'stock':c.Item.stock,
            }
            
    return JsonResponse(data)

# Cart Minus
def cart_minus(request):
    if request.method=='GET':
        id=request.GET['prod_id']
        i=AllProducts.objects.get(id=id)
        i.stock +=1
        i.save()
        c=Cart.objects.get(Q(Item=id) & Q(user=request.user))
        if  c.Quantity == 0:
            c.delete()
        else:
            c.Quantity =c.Quantity - 1
            c.Item.price=c.Item.price*c.Quantity
            c.save()
        print(c.Item.price)
        amount=0.00
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            temp_amount=(p.Quantity*p.Item.price)
            amount +=temp_amount
            total_amount=amount+shipping_amount
            print(temp_amount)        
            data={
                'quantity':c.Quantity,
                'amount':amount,
                'total_amount':total_amount,
                'item_total_price':c.Item.price,
                'stock':i.stock,
            }  
    return JsonResponse(data)


# Remove Item From The Cart
def removeItem(request):
    if request.method=='GET':
        id=request.GET['prod_id']
        c=Cart.objects.get(Q(Item=id) & Q(user=request.user))
        c.Item.price=c.Item.price*c.Quantity
        c.delete()
        amount=0.00
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            temp_amount=(p.Quantity*p.Item.price)
            amount +=temp_amount
            total_amount=amount+shipping_amount
            print(temp_amount)        
        data={
            'quantity':c.Quantity,
            'amount':amount,
            'total_amount':total_amount,
            'status':200,
            'item_total_price':c.Item.price,
        }
            
    return JsonResponse(data)



def buy_now(request):
    total_items=0
    if request.user.is_authenticated:
        total_items=len(Cart.objects.filter(user=request.user))
    context={
        'total_items':total_items,
    }
    return render(request, 'app/buynow.html' , context)

def profile(request):
    total_items=0
    if request.user.is_authenticated:
        total_items=len(Cart.objects.filter(user=request.user))
    context={
        'total_items':total_items,
    }
    return render(request, 'app/profile.html' ,context)

def address(request):
    total_items=0
    if request.user.is_authenticated:
        total_items=len(Cart.objects.filter(user=request.user))
    context={
        'total_items':total_items,
    }
    return render(request, 'app/address.html' , context)

def orders(request):
    total_items=0
    if request.user.is_authenticated:
        total_items=len(Cart.objects.filter(user=request.user))
    context={
        'total_items':total_items,
    }
    return render(request, 'app/orders.html' , context)

def change_password(request):
    total_items=0
    if request.user.is_authenticated:
        total_items=len(Cart.objects.filter(user=request.user))
    context={
        'total_items':total_items,
    }
    return render(request, 'app/changepassword.html' , context)

def mobile(request):
    total_items=0
    if request.user.is_authenticated:
        total_items=len(Cart.objects.filter(user=request.user))
    context={
        'total_items':total_items,
    }
    return render(request, 'app/mobile.html' , context)

def checkout(request):
    total_items=0
    if request.user.is_authenticated:
        total_items=len(Cart.objects.filter(user=request.user))
    context={
        'total_items':total_items,
    }
    return render(request, 'app/checkout.html' , context)


