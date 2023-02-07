from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# All Products Model 
class AllProducts(models.Model):
    title=models.CharField(max_length=200)
    desc=models.CharField(max_length=400)
    img=models.ImageField(upload_to='imgs')
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    
    def __str__(self):
        return self.title
    
#  Cart Model 
class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE , related_name='user_cart')
    Item=models.ForeignKey(AllProducts, on_delete=models.CASCADE)
    Quantity=models.IntegerField(default=1)
    
    def __str__(self):
        return self.Item.title