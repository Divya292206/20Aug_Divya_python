from django.shortcuts import render,redirect
from django.contrib.auth import logout
from doctors.models import Doctor
from accounts.models import User
from appointments.models import Appointment
from medicalrecords.models import MedicalRecord
from django.utils.timezone import now

# Create your views here.

def doctor_dashboard(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('/login/')

    user = User.objects.get(id=user_id)

    # ✅ Ensure doctor exists
    doctor, created = Doctor.objects.get_or_create(user=user)

    # ✅ Doctor related appointments
    appointments = Appointment.objects.filter(
        doctor=doctor
    ).order_by('date', 'time')

    active_tab = request.GET.get('tab', 'dashboard')

    # 🔥 Upload medical record logic
    if request.method == 'POST' and 'diagnosis' in request.POST:
        patient_id = request.POST.get('patient_id')
        appointment_id = request.POST.get('appointment_id')
        diagnosis = request.POST.get('diagnosis')
        prescription = request.POST.get('prescription')
        report = request.FILES.get('report')

        MedicalRecord.objects.create(
            patient_id=patient_id,
            doctor=doctor,
            appointment_id=appointment_id,
            diagnosis=diagnosis,
            prescription=prescription,
            report=report
        )

        return redirect('/doctors/?tab=upload')

    return render(request, 'doctor_dashboard.html', {
        'doctor': doctor,
        'appointments': appointments,
        'active_tab': active_tab
    })


def userlogout(request):
    logout(request)
    return redirect('/login/')


def doctor_profile_tab(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('/login/')

    user = User.objects.get(id=user_id)

    # ✅ FIX HERE
    doctor, created = Doctor.objects.get_or_create(
        user=user,
        defaults={
            'specialization': '',
            'availability': ''
        }
    )

    if request.method == 'POST':
        doctor.specialization = request.POST.get('specialization')
        doctor.availability = request.POST.get('availability')
        doctor.save()

        return redirect(request.path)

    return render(request, 'doctor_dashboard.html', {
        'doctor': doctor
    })

def doctor_upcoming_appointments(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('/login/')

    user = User.objects.get(id=user_id)
    doctor = Doctor.objects.get(user=user)

    appointments = Appointment.objects.filter(
        doctor=doctor
    ).select_related('patient')

    print("Appointments:", appointments)  # DEBUG

    return render(request, 'doctor_dashboard.html', {
        'appointments': appointments
    })

from django.shortcuts import get_object_or_404, redirect
from appointments.models import Appointment

def approve_appointment(request, appt_id):
    appointment = get_object_or_404(Appointment, id=appt_id)
    appointment.status = 'Approved'
    appointment.save()
    return redirect(request.META.get('HTTP_REFERER', '/doctors/'))

def cancel_appointment(request, appt_id):
    appointment = get_object_or_404(Appointment, id=appt_id)
    appointment.status = 'Rejected'
    appointment.save()
    return redirect(request.META.get('HTTP_REFERER', '/doctors/'))
