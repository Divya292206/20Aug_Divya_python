from django.contrib import admin
from django.urls import path,include
from adminapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('patient_data/', views.patient_data, name='patient_data'),
    path('admin_doctors_data/', views.admin_doctors_data, name='admin_doctors_data'),
    path('admin_appointments/', views.admin_appointments, name='admin_appointments'),
    path('admin_medicalrecord/', views.admin_medicalrecord, name='admin_medicalrecord'),
    path('patient_delete/<int:id>/', views.patient_delete, name='patient_delete'),
    path('doctor_delete/<int:id>/', views.doctor_delete, name='doctor_delete'),
    path('userlogout/', views.userlogout, name='userlogout'),
]
