from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TherapistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    credentials = models.TextField(blank=True)
    services = models.ManyToManyField(Service, related_name='therapists')  # Dropdown field
    photo = models.ImageField(upload_to='profile_pics/', blank=True)

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