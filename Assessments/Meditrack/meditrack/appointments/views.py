from django.contrib.auth import logout
from django.shortcuts import render, redirect
from accounts.models import User
from doctors.models import Doctor
from .models import Appointment
from .forms import AppointmentForm

def p_dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/login/')

    cuser = User.objects.get(id=user_id)
    appointments = Appointment.objects.filter(patient=cuser)

    # Only users with doctor role
    doctors = Doctor.objects.all()  # Already correct
    # Ensure: doctor.user.role == 'doctor'
    doctors = doctors.filter(user__role='doctor')

    return render(request, 'p_dashboard.html', {
        'cuser': cuser,
        'appointments': appointments,
        'doctors': doctors
    })


def book_appointment(request, doctor_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/login/')

    patient = User.objects.get(id=user_id)
    doctor = Doctor.objects.get(id=doctor_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appt = form.save(commit=False)
            appt.patient = patient
            appt.doctor = doctor
            appt.status = 'Pending'
            appt.save()
            return redirect('/appointments/')
    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {
        'form': form,
        'doctor': doctor
    })

def userlogout(request):
    logout(request)
    return redirect('/login/')

    

