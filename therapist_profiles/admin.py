from django.contrib import admin
from .models import TherapistProfile

@admin.register(TherapistProfile)
class TherapistProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'credentials', 'services')