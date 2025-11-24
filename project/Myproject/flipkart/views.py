from django.shortcuts import render
from .forms import *

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=='POST':
        contact=contact_form(request.POST)
        if contact.is_valid():
            contact.save()
            print("record insert sucessfully")
        else:
            print(contact.errors)
            
    return render(request,"contact.html")

