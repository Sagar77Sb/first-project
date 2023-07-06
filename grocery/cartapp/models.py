from django.db import models
from django.contrib.auth.models import User
from django import forms

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='images/')


    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    amount=models.IntegerField(default=0)
    total_amt=models.IntegerField(default=0)

    def total_cost(self):
        return self.quantity*self.product.price
    
class CartItem(forms.ModelForm):
    class Meta:
        model=Cart
        fields='__all__'