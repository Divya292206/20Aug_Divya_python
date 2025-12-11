from django.db import models

# Create your models here.

class contactinfo(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    subject=models.CharField(max_length=20)
    msg=models.TextField()