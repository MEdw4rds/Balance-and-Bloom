from django.contrib import admin
from .models import BookingOneOnOne

# Register your models here.


@admin.register(BookingOneOnOne)
class BookingAdmin(admin.ModelAdmin):
    """
    Displays list of current bookings in the admin panel.
    allows searching by user and date.
    """

    list_display = ('user', 'date', 'therapist')
