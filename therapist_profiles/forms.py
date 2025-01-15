from django import forms
from .models import TherapistProfile, Availability


class TherapistProfileForm(forms.ModelForm):
    class Meta:
        model = TherapistProfile
        fields = ['bio', 'credentials', 'services', 'photo'] 


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['day', 'start_time', 'end_time']
