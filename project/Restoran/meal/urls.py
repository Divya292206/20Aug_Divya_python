from django.contrib import admin
from django.urls import path,include
from meal import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('booking/',views.booking),
    path('contact/',views.contact),
    path('menu/',views.menu),
    path('team/',views.team),
]
