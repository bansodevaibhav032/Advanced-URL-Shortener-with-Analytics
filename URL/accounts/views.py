from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST.get("username",None)
        password=request.POST.get("password",None)
        if username and password:
            user= auth.authenticate(request,username=username,password=password)
            if user:
                auth.login(request,user)
                return render(request,"home.html")                       
            return render(request,"login.html",{'data':"Incorrect Credantials"})
    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST.get("username",None)
        password=request.POST.get("password",None)
        email=request.POST.get("email",None)
        fname=request.POST.get("fname",None)
        lname=request.POST.get("lname",None)
        
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
        
        auth.login(request,user)
        return render(request,'home.html')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect("login")