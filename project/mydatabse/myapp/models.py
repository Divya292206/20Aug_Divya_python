from django.db import models

# Create your models here.

class userinfo(models.Model):
    name=models.CharField(max_length=50)    #varchar
    email=models.EmailField()
    mobile=models.BigIntegerField()
    dob=models.DateField()