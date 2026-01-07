from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from Customer.models import ArtistProfile
from django.core.mail import send_mail
from Artist_project import settings
from Customer.models import User
from Customer.models import Contact
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Hardcoded admin credentials
        if email == "admin@gmail.com" and password == "admin123":
            return redirect('admin_dashboard')  # Redirect to dashboard
        else:
            # Optional: you can just reload page if wrong
            return render(request, 'admin_login.html', {'error': 'Invalid credentials'})

    return render(request, 'admin_login.html')

def admin_dashboard(request):
     # Pending artists
    pending_artists = ArtistProfile.objects.filter(status='PENDING')    
    return render(request, 'admin_dashboard.html',{'pending_artists': pending_artists})

def admin_artists_list(request):
    artists = ArtistProfile.objects.select_related('user').all()
    return render(request, 'admin_artist-list.html', {'artists': artists})


# -----------------------
# Approve Artist
# -----------------------
def approve_artist(request, artist_id):
    try:
        artist = ArtistProfile.objects.get(id=artist_id)
        artist.status = 'APPROVED'
        artist.save()

        send_mail(
            subject="Your Artist Profile is Approved!",
            message=f"Hello {artist.user.full_name},\n\nYour artist profile has been approved by admin. You can now login.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[artist.user.email],
            fail_silently=False,
        )

    except ArtistProfile.DoesNotExist:
        pass

    # ✅ LIST PAGE PAR PACHU JAVU
    return redirect('admin_artists_list')


# -----------------------
# Reject Artist
# -----------------------
def reject_artist(request, artist_id):
    try:
        artist = ArtistProfile.objects.get(id=artist_id)
        artist.status = 'REJECTED'
        artist.save()

        send_mail(
            subject="Your Artist Profile is Rejected",
            message=f"Hello {artist.user.full_name},\n\nYour artist profile has been rejected by admin.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[artist.user.email],
            fail_silently=False,
        )

    except ArtistProfile.DoesNotExist:
        pass

    # ✅ LIST PAGE PAR PACHU JAVU
    return redirect('admin_artists_list')


def admin_customers_list(request):
    customers = User.objects.filter(user_type='customer')
    return render(request, 'admin_customer-list.html', {
        'customers': customers
    })

def admin_bookings_list(request):
    return render(request, 'admin_booking.html')

def admin_customer_view(request, id):
    customer = get_object_or_404(User, id=id, user_type='customer')
    return render(request, 'admin_customer-view.html', {
        'customer': customer
    })

def admin_customer_delete(request, id):
    if request.method == "POST":
        customer = get_object_or_404(User, id=id, user_type='customer')
        customer.delete()
    return redirect('admin_customers_list')

def admin_contact(request):
    contacts = Contact.objects.all().order_by('-created_at')
    return render(request, 'admin_contact.html', {'contacts': contacts})


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('admin_contact')

def userlogout(request):
    logout(request)
    return redirect('admin_login')