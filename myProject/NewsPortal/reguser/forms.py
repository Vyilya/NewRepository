from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image_profile', 'first_name', 'last_name', 'age', 'about_me']