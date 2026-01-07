from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ArtistProfile(models.Model):

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    category = models.CharField(max_length=100, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    def __str__(self):
        return self.user.email
    
class ArtistMedia(models.Model):
    artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='artist_media/images/', blank=True, null=True)
    video = models.FileField(upload_to='artist_media/videos/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.artist.user.username} media"





