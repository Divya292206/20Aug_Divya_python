from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.

def index(request):
    msg=""
    if request.method=='POST':
        unm=request.POST['email']
        pas=request.POST['password']

        user=userinfo.objects.filter(email=unm,password=pas)

        if user: #true
            print("sucessfully")
            msg="sucessfully"

            request.session['user']=unm   #generated session
            return redirect('home')
        else:
            print("Error!")
            msg="Error!"

    return render(request,'index.html',{'msg':msg})

def register(request):
    msg=''
    if request.method=='POST':
        email=request.POST['email']
        form = user_form(request.POST)
        if form.is_valid():
            if userinfo.objects.filter(email=email).exists():
                msg = "Email is already exits!"
            else:
                form.save()
                print('record imsertd')
                return redirect("/")
        else:
            print(form.errors)

    return render(request,'register.html',{'msg':msg})

def home(request):
    user = request.session.get("user")

    try:
        cur = userinfo.objects.get(email=user)
        return render(request, "home.html", {'cuser': cur.name})

    except userinfo.DoesNotExist:
        print("Error")
        # return redirect("/")   # ← THIS FIXES THE ERROR
    return render(request, "home.html")

def userlogout(request):
    logout(request)
    return redirect("/")