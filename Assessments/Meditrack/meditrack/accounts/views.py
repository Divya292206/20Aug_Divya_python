from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import User
from appointments.views import p_dashboard
from doctors.views import doctor_dashboard
from doctors.models import Doctor

# Create your views here.

def home(request):
    return redirect('user_dashboard')

def user_dashboard(request):
    return render(request, 'user_dashboard.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        role = request.POST['role']

        user = User.objects.create(
            name=name,
            email=email,
            phone=phone,
            password=password,
            role=role
        )

        if role == 'doctor':
            Doctor.objects.create(
                user=user,
                specialization="Not Set",
                availability="Not Set"
            )

        return redirect('/login/')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email, password=password).first()

        if user:
            request.session['user_id'] = user.id
            request.session['role'] = user.role

            if user.role == 'doctor':
                return redirect('/doctors/')
            else:
                return redirect('/appointments/')

        return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')