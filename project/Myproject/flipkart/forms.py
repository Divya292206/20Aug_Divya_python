from django import forms
from .models import *

class contact_form(forms.ModelForm):
    class Meta:
        model=contactinfo
        fields='__all__'
