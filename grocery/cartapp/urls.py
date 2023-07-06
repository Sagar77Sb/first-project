from django.urls import path,include
from .import views as v
app_name='cart'
urlpatterns =[
    path('products',v.productt,name='product'),
    path('addtocart/<int:pk>',v.add_cart,name='addtocart1')
]