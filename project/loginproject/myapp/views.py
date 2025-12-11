from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.

def login(request):
    msg=""
    if request.method=='POST':
        unm = request.POST["email"]
        pas= request.POST["password"]

        user=userinfo.objects.filter(email=unm,password=pas)

        if user:
            print("Sucessfully!!")
            msg="Sucessfully!!"
            request.session['user']=unm
            return redirect("home")
        else:
            print("Error!")
            msg="Error!"

    return render(request,'login.html',{'msg':msg})

def signup(request):
    if request.method=='POST':
        form = user_form(request.POST)
        if form.is_valid():
            form.save()
            print('record imsertd')
            return redirect("/")
        else:
            print(form.errors)

    return render(request,'signup.html')

def home(request):
    user = request.session.get("user")
    cuser=userinfo.objects.get(email=user)
    return render(request,'home.html',{'user':cuser.name})

def userlogout(request):
    logout(request)
    return redirect("/")