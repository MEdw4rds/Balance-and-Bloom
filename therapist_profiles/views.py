from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TherapistProfileForm
from .models import TherapistProfile

# Index view
def index(request):
    return render(request, 'therapist_profiles/index.html')

def create_or_update_profile(request):
    profile, created = TherapistProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = TherapistProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = TherapistProfileForm(instance=profile)
    return render(request, 'therapist_profile_form.html', {'form': form})

def view_profile(request, user_id):
    profile = TherapistProfile.objects.get(user_id=user_id)
    return render(request, 'therapist_profile.html', {'profile': profile})