from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST["email"]

        if password1 != password2:
            messages.info(request,'password do not match')            
        elif User.objects.filter(username=username).exists():
            messages.info(request,'Username taken')            
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email taken')            
        else:
            user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name=last_name);
            user.save();
            return redirect('login')
        return redirect('register')
    return render(request,'register.html')

def signup(request):    
    if request.method == "POST":
        name = request.POST["name"]        
        password = request.POST["password"]
        repassword = request.POST["re_password"]
        email = request.POST["email"]
        username = request.POST["email"]

        if password != repassword:
            messages.info(request,'password do not match')                       
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email taken')            
        else:
            user = User.objects.create_user(username = username, password = repassword, email = email, first_name = name);
            user.save();
            return redirect('librarylogin')
        return redirect('signup')
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def librarylogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('librarylogin')
    else:
        return render(request,'librarylogin.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
