from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-added_on"]

    def __str__(self):
        return f"{self.name} | {self.email} | {self.added_on}"
