from django.contrib import admin
from .models import TherapistProfile, Availability, Service

class TherapistProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'credentials', 'get_services', 'photo')
    
    def get_services(self, obj):
        return ", ".join([service.name for service in obj.services.all()])
    get_services.short_description = 'Services Offered'


class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('therapist', 'day', 'start_time', 'end_time')


admin.site.register(TherapistProfile, TherapistProfileAdmin)
admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(Service)
