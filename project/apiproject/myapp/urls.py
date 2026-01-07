from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('', views.getuser),
    path('getuserbyid/<int:id>/', views.getuserbyid),
    path('deletestid/<int:id>/', views.deletestid),
    path('createuser/', views.createuser),
    path('updateuser/<int:id>/', views.updateuser),
]