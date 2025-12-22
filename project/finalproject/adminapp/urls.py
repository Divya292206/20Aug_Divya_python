from django.contrib import admin
from django.urls import path,include
from adminapp import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_userdata/', views.adminuserdata, name='admin_userdata'),
    path('admin_notes/', views.admin_note, name='admin_notes'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_user_delete/<int:uid>/', views.admin_user_delete, name='admin_user_delete'),
    path('admin_note_approve/<int:nid>/', views.admin_note_approve, name='admin_note_approve'),
    path('admin_note_rejected/<int:nid>/', views.admin_note_rejected, name='admin_note_rejected'),
    path('admin_note_delete/<int:nid>/', views.admin_note_delete, name='admin_note_delete'),
    path('admin_contact/', views.contact, name='admin_contact'),
    path('contact_delete/<int:cid>/', views.contact_delete, name='contact_delete'),
    path('admin_notes_card/', views.admin_notes_card, name='admin_notes_card'),
    path('admin_user_view/<int:uid>/', views.admin_user_view, name='admin_user_view'),
]
