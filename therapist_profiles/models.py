from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_therapist_profile(sender, instance, created, **kwargs):
    if created:
        TherapistProfile.objects.create(user=instance)

class Service(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TherapistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    credentials = models.TextField(blank=True)
    services = models.ManyToManyField(Service, related_name='therapists', blank=True)
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

    def clean(self):
        # Ensure both start_time and end_time are not None
        if self.start_time is None or self.end_time is None:
            return  # Skip validation if fields are missing

        # Check that end_time is after start_time
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time.")

    def __str__(self):
        return f"{self.therapist.user.username} - {self.get_day_display()}: {self.start_time} to {self.end_time}"

    class Meta:
        ordering = ['day', 'start_time']
        verbose_name_plural = "Availability"