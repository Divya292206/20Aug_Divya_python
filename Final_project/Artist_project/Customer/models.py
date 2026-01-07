from django.db import models
from django.contrib.auth.models import User
from Artist.models import ArtistProfile

# ------------------------
# Custom User Model
# ------------------------
class User(models.Model):
    USER_TYPE = (
        ('artist', 'Artist'),
        ('customer', 'Customer'),
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=10, choices=USER_TYPE)


# ------------------------
# Artist Profile (Extra Fields)
# ------------------------
class ArtistProfile(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    category = models.CharField(max_length=100, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    

# ------------------------


class Booking(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,  # or models.CASCADE if you want deletion to remove booking
        related_name='customer_bookings',
        null=True,    # allow null
        blank=True    # allow empty in forms
    )
    artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE)
    event_date = models.DateField()
    city = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} → {self.artist.full_name}"
    

class ArtistMedia(models.Model):
    artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='artist_media/', blank=True, null=True)
    video = models.FileField(upload_to='artist_media/', blank=True, null=True)

    
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



