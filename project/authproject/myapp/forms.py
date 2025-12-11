from django import forms
from .models import *

class user_form(forms.ModelForm):
    class Meta:
        model = userinfo
        fields = '__all__'