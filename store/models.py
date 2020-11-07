from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    digital= models.BooleanField(default=True,null=True)
    #iamge

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transition_id = models.CharField(max_length=100,null = True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add =True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length= 100)
    zipcode = models.CharField(max_length = 100)
    date_added =models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.address

 
