from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def index(request):
    if request.method=='POST':
        user=userform(request.POST)
        if user.is_valid():
            user.save()
            print("Record inserted")
        else:
            print(user.errors)
    return render(request,'index.html')

def showdata(request):
    data = userinfo.objects.all()
    return render(request,'showdata.html',{'data':data})

def deletedata(request,id):
    uid=userinfo.objects.get(id=id)
    userinfo.delete(uid)
    return redirect("showdata")

def updatedata(request,id):
    uid=userinfo.objects.get(id=id)
    if request.method=='POST':
        user=userform(request.POST,instance=uid)
        if user.is_valid():
            user.save()
            print("Record updated")
            return redirect('showdata')
        else:
            print(user.errors)
    return render(request,'updatedata.html',{'uid':uid})