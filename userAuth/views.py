from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def login_page(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')


        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid User")
            return redirect("login")

        print(username , password)
        user=authenticate(username=username, password=password)

        if user is None:
            messages.error(request,"Invalid Password")
            return redirect("login")
        
        else:
            login(request,user)
            return redirect("home")
        
    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect("login")

def register(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(fname, lname, email,password)

        user= User.objects.filter(username=email)
        if user.exists():
            messages.info(request, "User Alredy Exists.")
            return render(request,"register.html")

        user= User.objects.create(
            first_name=fname,
            last_name=lname,
            username=email
        )

        user.set_password(password)
        user.save()
        

        messages.info(request, "User Created Successfully.")
        return redirect('login')
    return render(request,"register.html")


@login_required(login_url="login")
def home_page(request):
    return render(request, "home_test.html")