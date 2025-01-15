from django.shortcuts import render, redirect
from . import forms
from django.http import HttpResponse

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('success')
    else:
        form = forms.ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def success(request):
  return render(request, 'contact/success.html')