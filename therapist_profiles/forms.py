from django import forms
from .models import TherapistProfile, Availability, Service


class TherapistProfileForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = TherapistProfile
        fields = ['bio', 'credentials', 'services', 'photo']


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['day', 'start_time', 'end_time']