from http.client import PAYMENT_REQUIRED
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#Customer (id, full_name, picture, number, user_id)

class Customer(models.Model):
    full_name=models.CharField(max_length=15)
    #photo=models.ImageField(upload_to='./customer/')
    number=models.CharField(max_length=50)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)

#Cuisine (id, cuisine_name, type, description)
class Cuisine(models.Model):
    cuisine_name=models.CharField(max_length=15)
    type=models.CharField(max_length=10)
    description=models.CharField(max_length=50)


#Menu (id, food_name, food_price, unit, cuisine.id)
class Menu(models.Model):
    food_name=models.CharField(max_length=60)
    food_price=models.IntegerField()
    unit=models.IntegerField()
    cuisine=models.ForeignKey(Cuisine,on_delete=models.CASCADE,null=True)



#Order (id, customer.id, date_time, total_price, arrival_time)
class Order(models.Model):
    date_time=models.DateTimeField()
    total_price=models.IntegerField()
    arrival_time=models.DateTimeField()

#OrderItem (id, order.id, menu.id, quantity, price)
class OrderItem(models.Model):
    Order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    Menu=models.ForeignKey(Menu, on_delete=models.CASCADE,null=True)
    #Quantity=models.IntegerField()
    
#Payment (id, order.id, customer.id, payment_type)
class Payment(models.Model):
    Payment_type=models.IntegerField()#characterfield
    Order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)

    
    # Create your models here.
