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
            return redirect('success')
    else:
        form = forms.ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def success(request):
  return render(request, 'contact/success.html', {'message': 'Thank you for contacting us'})