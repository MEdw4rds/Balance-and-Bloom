from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(validators=[EmailValidator()])
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.CharField(widget=forms.Textarea)
    added_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} | {self.email}"
