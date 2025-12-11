from django.shortcuts import render
from .forms import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    return render(request,'booking.html')

def contact(request):
    if request.method == 'POST':
        con = contact_form(request.POST)
        if con.is_valid():
            con.save()
            print("inserted record")
        else:
            print(con.errors)
    return render(request,'contact.html')

def menu(request):
    return render(request,'menu.html')

def team(request):
    return render(request,'team.html')
