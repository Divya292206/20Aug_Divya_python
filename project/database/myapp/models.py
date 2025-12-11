from django.db import models

# Create your models here.

class contactform(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.TextField(max_length=40)
    msg=models.TextField(max_length=100)
