from django.db import models
from django.contrib.auth.models import User

class TherapistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    credentials = models.TextField(max_length=500, blank=True)
    services = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='therapist_photos/', blank=True, null=True)
    availability = models.JSONField(default=dict)  # Example: {"Monday": ["10:00-12:00", "14:00-16:00"]}

    def __str__(self):
        return self.user.username

