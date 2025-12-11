from django.db import models

# Create your models here.

class userinfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.BigIntegerField()
    password=models.CharField(max_length=15)
