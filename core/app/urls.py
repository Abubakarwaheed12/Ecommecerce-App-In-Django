from django.urls import path
from app import views
urlpatterns = [
    path('', views.home),
    path('product-detail/<int:id>', views.product_detail, name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart , name='cart'),
    path('plus/' , views.cart_plus , name='plus'),
    path('minus/' , views.cart_minus , name='minus'),
    
    # path('cart/', views.emptycart, name='empty_cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('checkout/', views.checkout, name='checkout'),
    path('productlisting', views.product_listing , name='productlisting'),
]
