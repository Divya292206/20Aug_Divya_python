from django.contrib import admin
from django.shortcuts import render
from django.urls import path,include
from Customer import views

urlpatterns = [
    path('', views.customer_dashboard, name='customer_dashboard'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('main_dashboard/', views.main_dashboard, name='main_dashboard'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search_artist/', views.search_artist, name='artist_search'),
    path('book_artist/<int:artist_id>/', views.book_artist, name='book_artist'),
    path('booking_success/', lambda request: render(request, 'booking_success.html'), name='booking_success'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
]