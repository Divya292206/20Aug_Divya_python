from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('notes/', views.notes, name='notes'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('otp_varify/', views.otp_varify, name='otp_varify'),
    path('userlogout/', views.userlogout, name='userlogout'),
]
