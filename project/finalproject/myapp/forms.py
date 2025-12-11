from django import forms
from .models import *

class NoteinfoForm(forms.ModelForm):
    class Meta:
        model = Noteinfo
        fields = ['name', 'email', 'phone', 'password']

class ContactinfoForm(forms.ModelForm):
   class Meta:
       model = contactinfo
       fields = ['name', 'email', 'subject', 'msg']


class updateform(forms.ModelForm):
   class Meta:
       model = Noteinfo
       fields = ['name','phone']

class notesdataform(forms.ModelForm):
   class Meta:
       model = notesdata
       fields = ['title','cate','file','desc']
       