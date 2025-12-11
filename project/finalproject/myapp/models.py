from django.db import models

# Create your models here.

class Noteinfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    password=models.CharField(max_length=100)


class notesdata(models.Model):
    submitted_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(Noteinfo,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    cate=models.CharField(max_length=100)
    file=models.FileField(upload_to='Notes_Data')
    desc=models.TextField()
    status_choices = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status=models.TextField(max_length=10, choices=status_choices, default='pending')
    updated_at = models.DateTimeField(blank=True, null=True)


class contactinfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    msg=models.TextField()
   


    
