from django.contrib import admin
from django.urls import path,include
from adminapp import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
]
