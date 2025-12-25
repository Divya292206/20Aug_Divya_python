from django.contrib import admin
from django.urls import path,include
from doctors import views

urlpatterns = [
    path('', views.doctor_dashboard, name='doctor_dashboard'),
    path('logout/', views.userlogout, name='userlogout'),
    path('profile/', views.doctor_profile_tab, name='doctor_profile_tab'),
    path('upcoming_appointments/', views.doctor_upcoming_appointments, name='doctor_upcoming_appointments'),
    path('appointments/approve/<int:appt_id>/', views.approve_appointment, name='appointment_approve'),
    path('appointments/cancel/<int:appt_id>/', views.cancel_appointment, name='appointment_cancel'),
]
    
