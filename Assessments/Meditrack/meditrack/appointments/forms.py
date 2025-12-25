from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full border px-3 py-2 rounded'}),
            'time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'w-full border px-3 py-2 rounded'},
                format='%H:%M'  # 24-hour format
            ),
        }
