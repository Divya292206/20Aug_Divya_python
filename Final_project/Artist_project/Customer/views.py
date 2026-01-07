from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import User, ArtistMedia
from .forms import UserSignupForm, ArtistProfileForm
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from Customer.models import ArtistProfile, Booking, Contact
from django.contrib import messages


# Create your views here.

# ================= CUSTOMER DASHBOARD =================
def customer_dashboard(request):
    return render(request, 'customer_dashboard.html')


# ================= MAIN DASHBOARD =================
def main_dashboard(request):
    return render(request, 'main_dashboard.html')


# -----------------------
# SIGNUP
# -----------------------
def signup(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        user_type = request.POST['user_type']

        user = User.objects.create(
            full_name=full_name,
            email=email,
            mobile=mobile,
            password=make_password(password),  # ✅ HASHED
            user_type=user_type
        )

        if user_type == "artist":
            ArtistProfile.objects.create(
                user=user,
                category=request.POST.get('category'),
                experience=request.POST.get('experience') or 0,
                bio=request.POST.get('bio'),
                status='PENDING'
            )

        return redirect('login')

    return render(request, 'signup.html')


# -----------------------
# LOGIN
# -----------------------
def login_view(request):
    error = ""
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': "Invalid email or password"})

        if not check_password(password, user.password):
            return render(request, 'login.html', {'error': "Invalid email or password"})

        # Artist check
        if user.user_type == 'artist':
            try:
                artist_profile = ArtistProfile.objects.get(user=user)
            except ArtistProfile.DoesNotExist:
                return render(request, 'login.html', {'error': "Artist profile not found"})

            if artist_profile.status != 'APPROVED':
                if artist_profile.status == 'PENDING':
                    return render(request, 'login.html', {'error': "Your profile is under admin review."})
                elif artist_profile.status == 'REJECTED':
                    return render(request, 'login.html', {'error': "Your profile was rejected by admin."})

            request.session['user_id'] = user.id
            request.session['user_type'] = 'artist'
            return redirect('artist_dashboard')

        # Customer login
        request.session['user_id'] = user.id
        request.session['user_type'] = 'customer'
        return redirect('main_dashboard')

    return render(request, 'login.html', {'error': error})


# ================= LOGOUT =================
def logout_view(request):
    logout(request)
    return redirect('login')


# ================= STATIC PAGES =================
def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(request, "Message sent successfully!")
        return redirect('contact')
    return render(request, 'contact.html')


def search_artist(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')

    artists = ArtistProfile.objects.filter(status='APPROVED')

    if query:
        artists = artists.filter(
            Q(full_name__icontains=query)
        )

    if category:
        artists = artists.filter(category__iexact=category)

    return render(request, 'search_artists.html', {
        'artists': artists
    })
    
from django.shortcuts import render, get_object_or_404
from Artist.models import ArtistMedia
from Customer.models import ArtistProfile, Booking



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking
from .models import ArtistProfile  # to get the artist if needed

def book_artist(request, artist_id):
    # Get the artist for display
    artist = ArtistProfile.objects.get(id=artist_id, status='APPROVED')

    if request.method == "POST":
        event_date = request.POST.get('event_date')
        city = request.POST.get('city')
        message_text = request.POST.get('message')

        # Create booking without user/session
        Booking.objects.create(
            artist=artist,
            event_date=event_date,
            city=city,
            message=message_text or "",
            status='PENDING'
        )

        messages.success(request, "Booking request sent successfully!")
        return redirect(f"/book_artist/{artist_id}/")

    return render(request, 'book_artist.html', {'artist': artist})


def my_bookings(request):
    # Fetch all bookings (simple version)
    bookings = Booking.objects.all().order_by('-created_at')

    return render(request, 'my_bookings.html', {
        'bookings': bookings
    })




def booking_success(request):
    return render(request, 'booking_success.html')