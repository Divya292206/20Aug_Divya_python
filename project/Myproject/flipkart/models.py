from django.db import models

# Create your models here.

class contactinfo(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    msg=models.TextField(max_length=500)