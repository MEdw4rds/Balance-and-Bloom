from django.shortcuts import render, redirect
from . import forms
from django.http import HttpResponse
from django.core.mail import send_mail
import csv
from .models import Contact

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            sname = form.cleaned_data['name']
            semail = form.cleaned_data['email']
            smessage = form.cleaned_data['message']
            sfile = open('responses.csv', 'a')
            swriter = csv.writer(sfile)
            swriter.writerow([sname,semail,smessage])
            sfile.close()
            sphone = form.cleaned_data['phone']
            ssubject = form.cleaned_data['subject']
            smessage = form.cleaned_data['message']
            sadmin_email = "awellness9998@yahoo.com"
            # Send an email
            #send_mail(
               # f'From {name}, Subject: {subject}',
              #  f'Message: {message}\nContact Phone: {phone}',
               # email,  # From email
              #  [admin_email],  # To email
             #   fail_silently=False,
            #)
            save_form=Contact(name=sname,email=semail,phone=sphone, subject=ssubject, message=smessage)
            save_form.save()
            return redirect('success')
    else:
        form = forms.ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def success(request):
  return render(request, 'contact/success.html', {'message': 'Thank you for contacting us'})