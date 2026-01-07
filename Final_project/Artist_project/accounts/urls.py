from django.contrib import admin
from django.urls import path,include
from accounts import views

urlpatterns = [
    path('', views.login_view, name='admin_login'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/artists/', views.admin_artists_list, name='admin_artists_list'),
    path('admin/customers/', views.admin_customers_list, name='admin_customers_list'),
    path('admin/bookings/', views.admin_bookings_list, name='admin_booking'),
    path('admin/approve_artist/<int:artist_id>/', views.approve_artist, name='approve_artist'),
    path('admin/reject_artist/<int:artist_id>/', views.reject_artist, name='reject_artist'),
    path('admin/customers/view/<int:id>/', views.admin_customer_view, name='admin_customer_view'),
    path('admin/customers/delete/<int:id>/', views.admin_customer_delete, name='admin_customer_delete'),
    path('admin/admin_contact/', views.admin_contact, name='admin_contact'),
    path('admin/delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('admin/userlogout/',views.userlogout, name='userlogout'),  
]