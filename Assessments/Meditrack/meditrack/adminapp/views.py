from django.shortcuts import render,redirect
from django.contrib.auth import logout
from accounts.models import User
from appointments.models import Appointment
from django.utils.timezone import now
from medicalrecords.models import MedicalRecord
from django.shortcuts import render, redirect, get_object_or_404
from doctors.models import Doctor


#Create Your frist View

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Hardcoded admin credentials
        if email == "admin@gmail.com" and password == "admin123":
            return redirect('admin_dashboard')  # Redirect to dashboard
        else:
            # Optional: you can just reload page if wrong
            return render(request, 'index.html')

    return render(request, 'index.html')


def admin_dashboard(request):
    total_doctor = Doctor.objects.count()
    total_patient = User.objects.filter(role='patient').count()

    return render(request, 'admin_dashboard.html', {'total_doctor': total_doctor,'total_patient': total_patient,})

def patient_data(request):
    patients = User.objects.filter(role='patient')

    return render(request, 'patient_data.html', {'patients': patients})

def admin_doctors_data(request):
    doctors = User.objects.filter(role='doctor')

    return render(request, 'admin_doctors_data.html', {'doctors': doctors})

def admin_appointments(request):
    appointments = Appointment.objects.all()

    status = request.GET.get('status')

    if status and status != 'all':
        appointments = Appointment.objects.filter(status=status)
    else:
        appointments = Appointment.objects.all()

    

    return render(request, 'admin_appointments.html', {'appointments': appointments})


def admin_medicalrecord(request):
    medicalrecords = MedicalRecord.objects.all()
    context = {
        'medicalrecords': medicalrecords,
    }
    return render(request, 'admin_medicalrecord.html', context)




# Delete patient
def patient_delete(request, id):
    patient = get_object_or_404(User, id=id, role='patient')
    patient.delete()
    return redirect('patient_data')

# Delete doctor
def doctor_delete(request, id):
    doctor = get_object_or_404(User, id=id, role='doctor')
    doctor.delete()
    return redirect('admin_doctors_data')

def userlogout(request):
    logout(request)
    return redirect('login')



