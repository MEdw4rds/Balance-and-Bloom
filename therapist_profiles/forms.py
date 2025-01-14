from django import forms
from .models import TherapistProfile

class TherapistProfileForm(forms.ModelForm):
    class Meta:
        model = TherapistProfile
        fields = ['bio', 'credentials', 'services', 'photo', 'availability']
