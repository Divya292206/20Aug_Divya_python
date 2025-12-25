from django.urls import path
from . import views

urlpatterns = [
    path('', views.p_dashboard, name='p_dashboard'),
    path('book_appointment/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('logout/', views.userlogout, name='userlogout'),
]
