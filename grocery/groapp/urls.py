from django.urls import path
from . import views
from django.conf import settings

urlpatterns =[
    path("/",views.home,name="home"),
    path("registration",views.registration,name="register"),
    path("user_login",views.userlogin,name="logins"),
    path("dashboard",views.user_dashboard,name="dashboards"),
    path("logout",views.logoutt,name="logouts")
]