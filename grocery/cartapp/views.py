from django.shortcuts import render,redirect,HttpResponse
from .models import *

def productt(request):
    obj=Product.objects.all()
    d={'product':obj}
    return render(request,'products.html',d)

    
def add_cart(request,pk):
    user_id=request.session.get("id")
    user=request.user
    if request.method=='GET':
        product=Product.objects.get(id=pk)
        Cart(user=user,product=product).save()
        return redirect("/cartapp-products")

def show_cart(request):
    ids=request.session.get("id")
    obj=Cart.objects.filter(user=ids)
    amount=0
    value=0
    for p in obj:
        value=p.quantity*p.product.price
        amount=value+amount
        total_amount= amount + 45
        d={'data':obj,'total_amount':total_amount,'amount':amount}
        return render(request,'carts.html',d)
    
def delete(request,proid):
    obj=Cart.objects.get(id=proid)
    obj.delete()
    return redirect("/cartapp-showcart")


def plus_cart(request,pid):
   if request.method=='GET': 
    c=Cart.objects.get(id=pid)
    c.quantity +=1
    c.save()
    user=request.user
    cart=Cart.objects.filter(user=user)
    for i in cart:
        amount=0
        value= i.quantity*i.product.price
        amount=amount+ value
        total_amount=amount + 45
        data={"quantity":c.quantity,"amount":c.amount,"total_amount":c.total_amount}
        return redirect("/cartapp-showcart")
    
def plus_cart(request,pid):
   if request.method=='GET': 
    c=Cart.objects.get(id=pid)
    c.quantity -=1
    c.save()
    user=request.user
    cart=Cart.objects.filter(user=user)
    for i in cart:
        amount=0
        value= i.quantity*i.product.price
        amount=amount+ value
        total_amount=amount + 45
        data={"quantity":c.quantity,"amount":c.amount,"total_amount":c.total_amount}
        return redirect("/cartapp-showcart")

