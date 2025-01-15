from django import forms
from .models import BookingOneOnOne


class BookingForm(forms.ModelForm):
    """
    Creates form to be displayed in :view:`booking.book_time_slot` applying a
    widget to the date field and using the date and timeslot fields.
    """
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = BookingOneOnOne
        fields = ['date', 'time_slot', 'therapist']


class EditBookingForm(forms.ModelForm):
    """
    Creates form to be displayed in :view:`booking.edit_booking` applying a
    widget to the date field and using the date and timeslot fields.
    """
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = BookingOneOnOne
        fields = ['date', 'time_slot', 'therapist']
