from django.db import models
from django.contrib.auth.models import User

class TherapistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    credentials = models.TextField(max_length=500, blank=True)
    services = models.CharField(max_length=255, blank=True)
    photo = models.URLField(max_length=500, blank=True, null=True)
    availability = models.JSONField(default=dict)  # Example: {"Monday": ["10:00-12:00", "14:00-16:00"]}

    def __str__(self):
        return self.user.username

class TherapistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    credentials = models.TextField(blank=True)
    services = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='profile_pics/', blank=True)
    # Remove the availability field from here if you had one previously

    def __str__(self):
        return self.user.username


class Availability(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    therapist = models.ForeignKey(TherapistProfile, on_delete=models.CASCADE, related_name='availability')
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.therapist.user.username} - {self.day}: {self.start_time} to {self.end_time}"
