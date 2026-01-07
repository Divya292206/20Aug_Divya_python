from django import forms
from django.contrib.auth.hashers import make_password
from .models import User, ArtistProfile

# ---------------------------
# User Signup Form
# ---------------------------
class UserSignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'px-4 py-3 rounded-lg bg-black/40 border border-white/20 focus:outline-none'}),
        label="Password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'px-4 py-3 rounded-lg bg-black/40 border border-white/20 focus:outline-none'}),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['full_name', 'email', 'mobile', 'user_type']

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'px-4 py-3 rounded-lg bg-black/40 border border-white/20 focus:outline-none'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'px-4 py-3 rounded-lg bg-black/40 border border-white/20 focus:outline-none'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'px-4 py-3 rounded-lg bg-black/40 border border-white/20 focus:outline-none'}),
            'user_type': forms.RadioSelect(choices=User.USER_TYPE),
        }

    # Password validation
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

    # Save user with hashed password
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# ---------------------------
# Artist Profile Form
# ---------------------------
class ArtistProfileForm(forms.ModelForm):
    class Meta:
        model = ArtistProfile
        fields = ['category', 'experience', 'bio']

        widgets = {
            'category': forms.TextInput(attrs={'placeholder': 'Artist Category (Singer, Dancer, etc.)', 'class': 'px-4 py-3 rounded-lg bg-black/40 border border-white/20 focus:outline-none'}),
            'experience': forms.NumberInput(attrs={'placeholder': 'Experience (Years)', 'class': 'px-4 py-3 rounded-lg bg-black/40 border border-white/20 focus:outline-none'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Short Bio', 'class': 'px-4 py-3 rounded-lg bg-black/40 border border-white/20 focus:outline-none'}),
        }
