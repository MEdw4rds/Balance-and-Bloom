from django.db import models
from therapist_profiles.models import TherapistProfile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime
from datetime import date


class BookingOneOnOne(models.Model):
    """
    Stores a single booking entry related to :model:`auth.User`.
    """
    TIMESLOTS = [
        (datetime.time(hour=8), '08:00'),
        (datetime.time(hour=8, minute=30), '08:30'),
        (datetime.time(hour=9), '09:00'),
        (datetime.time(hour=9, minute=30), '09:30'),
        (datetime.time(hour=10), '10:00'),
        (datetime.time(hour=10, minute=30), '10:30'),
        (datetime.time(hour=11), '11:00'),
        (datetime.time(hour=11, minute=30), '11:30'),
        (datetime.time(hour=13), '13:00'),
        (datetime.time(hour=13, minute=30), '13:30'),
        (datetime.time(hour=14), '14:00'),
        (datetime.time(hour=14, minute=30), '14:30'),
        (datetime.time(hour=15), '15:00'),
        (datetime.time(hour=15, minute=30), '15:30'),
        (datetime.time(hour=16), '16:00'),
        (datetime.time(hour=16, minute=30), '16:30'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField(choices=TIMESLOTS)
    therapist = models.ForeignKey(TherapistProfile, on_delete=models.RESTRICT)

    class Meta:
        unique_together = ['date', 'time_slot']

    def clean(self):
        super().clean()
        if self.date < datetime.date.today():
            raise ValidationError('You cannot book a past date.')

    def save(self, *args, **kwargs):
        # Check the number of bookings for this user in the current month
        current_month_bookings = BookingOneOnOne.objects.filter(
            user=self.user,
            date__year=date.today().year,
            date__month=date.today().month
        ).count()

        # Define the booking limit
        booking_limit = 8  # You can change this to your desired limit

        if current_month_bookings >= booking_limit:
            raise ValueError(
                f"You have exceeded the booking limit of {booking_limit} "
                f"per month."
            )
        super(BookingOneOnOne, self).save(*args, **kwargs)
