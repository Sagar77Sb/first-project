from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout 
from .models import *
from .forms import *

def home(request):
    return render(request,'home.html')

def registration(request):
    if request.method=='POST':
        obj= UserCreationForm(request.POST)
        obj.save()
        return redirect("/kitchen-user_login")
    else:
        d={'form':UserCreationForm}
        return render(request,'register.html',d)

def userlogin(request):
    if request.method=='POST':
        uname=request.POST.get("username")
        passwd=request.POST.get("password")
        users=authenticate(request,username=uname,password=passwd)
        if users is not None:
            request.session["id"]=users.id
            print(request.session.get("id"))
            login(request,users)
            return redirect("/kitchen-dashboard")
        else:
            d={'form':LoginForm}
            return render(request,'login.html',d)
    else:
            d={'form':LoginForm}
            return render(request,'login.html',d)

def user_dashboard(request):
    if request.method=='POST':
        user_id=request.session.get("id")
        obj_user=User.objects.get(id=user_id)
        obj=RegistrationForm(request.POST)
        data=obj.save(commit=False)
        data.user=obj_user
        data.save()
        return redirect("/kitchen-dashboard")
    else:
        d={'forms':RegistrationForm}
        return render(request,'dashboard.html',d)


def logoutt(request):
    logout(request)
    return redirect("/")
