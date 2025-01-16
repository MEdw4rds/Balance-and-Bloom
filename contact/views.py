from django.shortcuts import render, redirect
from . import forms
from django.http import HttpResponse
from django.core.mail import send_mail
import csv

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            file = open('responses.csv', 'a')
            writer = csv.writer(file)
            writer.writerow([name,email,message])
            file.close()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            admin_email = "awellness9998@yahoo.com"
            # Send an email
            send_mail(
                f'From {name}, Subject: {subject}',
                f'Message: {message}\nContact Phone: {phone}',
                email,  # From email
                [admin_email],  # To email
                fail_silently=False,
            )

            return redirect('success')
    else:
        form = forms.ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def success(request):
  return render(request, 'contact/success.html', {'message': 'Thank you for contacting us'})