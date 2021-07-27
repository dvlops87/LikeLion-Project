from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.

class User(AbstractUser):
    university = models.CharField(max_length=20, default='')
    userImage = models.ImageField(upload_to='userImage/',blank=True, null=True)

class Product(models.Model):
    productName = models.CharField(max_length=50, default='')
    productDetail = models.TextField(default='')
    productImage = models.ImageField(upload_to="productImage/",blank=True, null=True)
    productPrice =  models.CharField(max_length=50, default='')
    def __str__(self):
        return str(self.productName)

class OrderList(models.Model):
    orderUser = models.ForeignKey('shopping.User', on_delete=models.CASCADE, default='')
    productOrder = models.ForeignKey('shopping.Product', on_delete=models.CASCADE, default='')
    def __str__(self):
        return str(self.productOrder)