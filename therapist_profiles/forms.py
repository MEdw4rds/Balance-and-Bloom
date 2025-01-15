from django import forms
from .models import TherapistProfile

class TherapistProfileForm(forms.ModelForm):
    # Services field as a Multi-Select Dropdown
    SERVICES_CHOICES = [
        ('counseling', 'Counseling'),
        ('therapy', 'Therapy'),
        ('coaching', 'Coaching'),
    ]

    services = forms.MultipleChoiceField(
        choices=SERVICES_CHOICES,
        widget=forms.CheckboxSelectMultiple,  # Use Checkbox or Multi-Select dropdown
    )

    class Meta:
        model = TherapistProfile
        fields = ['bio', 'credentials', 'services', 'photo', 'availability']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
