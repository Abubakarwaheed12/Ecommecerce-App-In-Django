from django.urls import path
from . import views
urlpatterns=[
    path('login', views.loginuser, name='login'),
    path('registration', views.customerregistration, name='customerregistration'),
]