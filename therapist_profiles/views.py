from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TherapistProfileForm
from .models import TherapistProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Index view
def index(request):
    return render(request, 'therapist_profiles/index.html')

@login_required
def create_or_update_profile(request):
    # Get or create the profile for the current user
    profile, created = TherapistProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = TherapistProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('therapist_profile')  # Redirect to the profile details page
    else:
        form = TherapistProfileForm(instance=profile)
    
    return render(request, 'therapist_profiles/therapist_profile_form.html', {'form': form})
    
def view_profile_by_id(request, user_id):
    profile = get_object_or_404(TherapistProfile, user_id=user_id)
    return render(request, 'therapist_profiles/therapist_profile.html', {'profile': profile})

def view_profile_by_username(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(TherapistProfile, user=user)
    return render(request, 'therapist_profiles/therapist_profile.html', {'profile': profile})

def view_profile(request):
    if not request.user.is_authenticated:
        return redirect('account_login')  # Redirect to login if user is not authenticated

    # Get the profile or handle the case where it doesn't exist
    try:
        profile = TherapistProfile.objects.get(user=request.user)
    except TherapistProfile.DoesNotExist:
        # Redirect to the profile creation form if no profile exists
        return redirect('create_or_update_profile')

    return render(request, 'therapist_profiles/therapist_profile.html', {'profile': profile})

