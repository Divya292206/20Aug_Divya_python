from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def admin_home(request):
    return render(request, 'admin_home.html')