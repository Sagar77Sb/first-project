from django.urls import path,include
from .import views as v
app_name='cart'
urlpatterns =[
    path('products',v.productt,name='product'),
    path('addtocart/<int:pk>',v.add_cart,name='addtocart1'),
    path('showcart',v.show_cart,name='showcart1'),
    path("del/<int:proid>",v.delete,name='delete1')
]