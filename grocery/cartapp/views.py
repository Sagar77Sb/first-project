from django.shortcuts import render,redirect
from .models import *

def productt(request):
    obj=Product.objects.all()
    d={'product':obj}
    return render(request,'products.html',d)

    
def add_cart(request,pk):
    user_id=request.session.get("id")
    user=request.user
    if request.methos=='GET':
        product=Product.objects.get(id=pk)
        Cart(user=user,product=product).save()
        return redirect("/cartapp-products")

def show_cart(request):
    ids=request.session.get("id")
    obj=Cart.objects.filter(id=ids)
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




