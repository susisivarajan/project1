from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse("hai")
def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        password1=request.POST["password1"]
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect("home")
            elif User.objects.filter(email=email).exists():
                    messages.info(request, "email already exists")
                    return redirect("home")
            else:

                        user=User.objects.create_user(username=username,email=email,password=password)
                        user.save()
                        messages.info(request,"registration successful")
        else:
            messages.info(request,"password not match")
            return redirect("home")
        return redirect("login")
    return render(request,"home.html")
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("index")
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")
    return render(request,"login.html")






