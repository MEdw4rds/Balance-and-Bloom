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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add the 'form-control' class to all fields except 'services' (since it's a CheckboxSelectMultiple)
        for field_name, field in self.fields.items():
            if field_name != 'services':  # Skip 'services' since it's a multi-checkbox
                field.widget.attrs['class'] = 'form-control'


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['day', 'start_time', 'end_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add the 'form-control' class to all fields in AvailabilityForm
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
