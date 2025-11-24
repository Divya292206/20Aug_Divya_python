from django import forms
from .models import *

class userform(forms.ModelForm):
    class Meta:
        model=userinfo
        fields='__all__'