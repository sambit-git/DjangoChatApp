from django import forms
from .models import UserProfile

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']