from django.db import models
from django.db.models.expressions import F
from django.db.models.query_utils import PathInfo 
from django.contrib.auth.models import User 


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

class Product(models.Model): 
    product_name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=1500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    note = models.CharField(max_length=1000, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

class Order(models.Model):   
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    number_phone = models.CharField(max_length=10, null=True) #change null 
    address = models.CharField(max_length=100, null=True)
    total_price = models.DecimalField(max_digits=9, decimal_places=0, null=True, blank=True)
    note = models.TextField(max_length=500, null=True)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    image = models.URLField(max_length=200)

    def __str__(self):
        return str(self.product)
 