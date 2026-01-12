from django.shortcuts import render
from rest_framework import viewsets
from .models import Restaurant,MenuItem
from .serializers import RestaurantSerializer,MenuItemSerializer

# Create your views here.

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer



