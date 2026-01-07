from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Artist.models import ArtistProfile
from Artist.models import ArtistMedia
from Customer.models import Booking
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_POST


# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Customer.models import ArtistProfile

def artist_profile(request):
    # Get the logged-in artist
    artist = get_object_or_404(ArtistProfile, user_id=request.session['user_id'])
    if request.method == "POST":
        # Update fields from the form
        full_name = request.POST.get('full_name')
        mobile = request.POST.get('mobile')
        bio = request.POST.get('bio')

        # Update the related User fields
        user = artist.user
        if full_name:
            user.full_name = full_name
        if mobile:
            user.mobile = mobile
        user.save()

        # Update artist-specific fields
        if bio:
            artist.bio = bio
        artist.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('artist_profile')

    # GET request: render form with existing data
    
    return render(request, 'artist_profile.html', {'artist': artist})


def artist_dashboard(request):
   return render(request, 'artist_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def artist_media_gallery(request):

    if request.method == "POST":
        file = request.FILES.get('media')

        if file:
            if file.content_type.startswith('video'):
                ArtistMedia.objects.create(
                    video=file
                )
            else:
                ArtistMedia.objects.create(
                    image=file
                )

        return redirect('artist_media')

    media_files = ArtistMedia.objects.filter()

    return render(request, 'artist_media.html', {'media_files': media_files})



def delete_media(request, media_id):
    media = get_object_or_404(ArtistMedia, id=media_id)
    media.delete()
    return redirect('artist_media')



def artist_bookings(request):
    # get logged-in artist

    # only this artist's bookings
    bookings = Booking.objects.filter().order_by('-created_at')

    return render(request, 'artist_bookings.html', {
        'bookings': bookings
    })


def approve_booking(request, booking_id):

    # 🔒 Ensure logged-in user is an artist
    try:
        artist = ArtistProfile.objects.get(user=request.user)
    except ArtistProfile.DoesNotExist:
        return HttpResponseForbidden("Access Denied")

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        artist=artist
    )

    booking.status = 'APPROVED'
    booking.save()

    # 📩 EMAIL TO CUSTOMER
    customer_name = booking.customer.get_full_name() or booking.customer.username

    send_mail(
        subject="🎉 Your Booking is Approved | Artist Hub",
        message=f"""
Hello {customer_name},

Great news! 🎶

Your booking has been APPROVED by:
Artist: {artist.user.get_full_name()}

📅 Event Date: {booking.event_date}
📍 Location: {booking.city}

The artist will contact you soon.

Thank you for using Artist Hub.
""",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[booking.customer.email],
        fail_silently=False,
    )

    return redirect('artist_bookings')



def reject_booking(request, booking_id):

    try:
        artist = ArtistProfile.objects.get(user=request.user)
    except ArtistProfile.DoesNotExist:
        return HttpResponseForbidden("Access Denied")

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        artist=artist
    )

    booking.status = 'REJECTED'
    booking.save()

    # 📩 EMAIL TO CUSTOMER
    customer_name = booking.customer.get_full_name() or booking.customer.username

    send_mail(
        subject="❌ Booking Rejected | Artist Hub",
        message=f"""
Hello {customer_name},

We’re sorry to inform you that your booking request has been REJECTED.

Artist: {artist.user.get_full_name()}
📅 Event Date: {booking.event_date}

You can search and book another artist anytime.

Thank you,
Artist Hub Team
""",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[booking.customer.email],
        fail_silently=False,
    )

    return redirect('artist_bookings')



