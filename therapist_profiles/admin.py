from django.contrib import admin
from .models import TherapistProfile, Availability, Service


# Define Availability as an Inline Admin
class AvailabilityInline(admin.TabularInline):  # Use StackedInline for vertical layout if preferred
    model = Availability
    extra = 1  # Number of empty rows for adding new availability
    can_delete = True


class TherapistProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'credentials', 'get_services', 'photo')
    filter_horizontal = ('services',)  # Adds a widget for selecting multiple services in the admin panel

    def get_services(self, obj):
        return ", ".join([service.name for service in obj.services.all()])
    get_services.short_description = 'Services Offered'


# Customize Availability Admin (Optional if you want to keep it separate too)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('therapist', 'day', 'start_time', 'end_time')


# Register models
admin.site.register(TherapistProfile, TherapistProfileAdmin)
admin.site.register(Availability, AvailabilityAdmin)  # Optional if you want to manage Availability separately
admin.site.register(Service)
