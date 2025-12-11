from django import forms
from .models import contactform

class ContactForm(forms.ModelForm):
    class Meta:
        model = contactform
        fields = '__all__'
