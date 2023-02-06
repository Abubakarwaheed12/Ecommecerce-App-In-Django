from django.db import models

# Create your models here.

class AllProducts(models.Model):
    title=models.CharField(max_length=200)
    desc=models.CharField(max_length=400)
    img=models.ImageField(upload_to='imgs')
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    
    def __str__(self):
        return self.title