from django.contrib import admin
from .models import TherapistProfile, Availability

class AvailabilityInline(admin.TabularInline):
    model = Availability
    extra = 1

@admin.register(TherapistProfile)
class TherapistProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'credentials', 'services')
    inlines = [AvailabilityInline]
