from django.contrib import admin
from django.urls import path,include
from Artist import views

urlpatterns = [
    path('artist_dashboard/', views.artist_dashboard, name='artist_dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('artist_profile/', views.artist_profile, name='artist_profile'),
    path('artist_media/', views.artist_media_gallery, name='artist_media'),
    path('delete_media/<int:media_id>/', views.delete_media, name='delete_media'),
    path('artist/artist_bookings/', views.artist_bookings, name='artist_bookings'),
    path('approve_booking/<int:booking_id>/', views.approve_booking, name='approve_booking'),
    path('reject_booking/<int:booking_id>/', views.reject_booking, name='reject_booking'),
]