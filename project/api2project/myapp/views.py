from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    req = requests.get('https://fakestoreapi.com/products')
    data = req.json()
    return render(request, 'index.html', {'data': data})