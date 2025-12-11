from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import *

# Create your views here.

def index(request):
    if request.method=='POST':
        contact=ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            print("record inserted")
        else:
            print(contact.errors)

    
    return render(request,'index.html')

def showdata(request):
    data=contactform.objects.all()
    return render(request,'showdata.html',{'data':data})

def deletedata(request,id):
    cid = contactform.objects.get(id=id)
    contactform.delete(cid)
    return redirect("showdata")

def updatedata(request,id):
    uid = contactform.objects.get(id=id)
    if request.method=='POST':
        contact=ContactForm(request.POST,instance=uid)
        if contact.is_valid():
            contact.save()
            print("record inserted")
            return redirect("showdata")
        else:
            print(contact.errors)

    return render(request,'updatedata.html',{'uid':uid})

