from django.urls import path
from . import views
urlpatterns=[
    path('login', views.loginuser, name='login'),
    path('registration', views.customerregistration, name='customerregistration'),
    path('logout', views.logoutuser , name='logout' ),
    path('forgotPassword' , views.ForgetPassword , name='forgotPassword'),
    path('resetPassword/<token>' , views.ChangePassword , name='resest_password'),
]