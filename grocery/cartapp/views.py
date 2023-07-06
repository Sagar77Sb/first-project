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

