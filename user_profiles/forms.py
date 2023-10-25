
from django import forms
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'history']
        widgets = {
            'history': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }
