from django.contrib import admin
from django.urls import path,include
from flipkart import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
]
