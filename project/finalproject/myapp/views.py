from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
from finalproject import settings
import random
from .models import *
from django.contrib.auth import logout

# Create your views here.

def index(request):
    user = request.session.get('email')

    return render(request, 'index.html', {'user': user})

def about(request):
    user = request.session.get('email')

    return render(request, 'about.html', {'user': user})

def contact(request):
    user = request.session.get('email')

    return render(request, 'contact.html', {'user': user})

def login(request):  
    msg=""
    if request.method=="POST":
        enm=request.POST['email']
        pas=request.POST['password']
        user = Noteinfo.objects.filter(email=enm,password=pas)
        userid = Noteinfo.objects.get(email=enm)
        if user:
            print("login successful")
            msg = "Login successful"

            request.session['email']=enm  #session created
            request.session['userid']=userid.id

            return redirect('/')
        else:
            print("Login failed! Invalid email or password.")
            msg = "Login failed! Invalid email or password."
    return render(request, 'login.html',{'msg':msg})


def notes(request):
    user = request.session.get('email')
    unm = Noteinfo.objects.get(email=user)
    if request.method == "POST":
        newreq = notesdataform(request.POST, request.FILES)
        if newreq.is_valid():
            x=newreq.save(commit=False)
            x.user=unm
            x.status='pending'
            x.save()
            print("sucessfully saved")
            return redirect("/")
        else:
            print(newreq.errors)

    return render(request, 'notes.html', {'user': user})

def signup(request):
    if request.method == "POST":
        form = NoteinfoForm(request.POST)
        if form.is_valid():
            form.save()
            print("sucessfully saved")

            global otp

            otp = random.randint(1111,9999)

            sub = "OTP Verification - NotesApp"
            msg = f"Dear User,\n\nThank you for registering with NotesApp!\nYour One-Time Password (OTP) for account verification is:\n\n🔐 OTP: {otp}"
            f_email = settings.EMAIL_HOST_USER
            to_email = [request.POST["email"]]

            send_mail(subject=sub,message=msg,from_email=f_email,recipient_list=to_email)

            return redirect('otp_varify')
        else:
            print("form.errors")
    return render(request, 'signup.html')

def profile(request):
    user = request.session.get('email')
    userid = request.session.get('userid')
    cuser = Noteinfo.objects.get(id=userid)

    if request.method == "POST":
        updatereq = updateform(request.POST,instance=cuser)
        if updatereq.is_valid():
            updatereq.save()
            print("sucessfully saved")
            return redirect('/')
        else:
            print(updatereq.errors)

    return render(request, 'profile.html', {'user': user, 'cuser': cuser})

def otp_varify(request):
    msg = ""
    if request.method == "POST":
        if request.POST['otp']==str(otp):
            print("OTP verified successfully")
            msg = "OTP verified successfully"
            return redirect('login')
        else:
            print("Invalid OTP. Please try again.")
            msg = "Invalid OTP. Please try again."
    return render(request, 'otp_varify.html', {'msg': msg})

def userlogout(request):
    logout(request)
    return redirect('login')

