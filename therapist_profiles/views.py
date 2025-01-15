from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TherapistProfileForm, AvailabilityForm
from .models import TherapistProfile, Availability
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import modelformset_factory

# Index view
def index(request):
    return render(request, 'therapist_profiles/index.html')

@login_required
def create_or_update_profile(request):
    profile, created = TherapistProfile.objects.get_or_create(user=request.user)

    # Handle the availability formset
    AvailabilityFormSet = modelformset_factory(
        Availability, 
        form=AvailabilityForm, 
        extra=1, 
        can_delete=True
    )

    # Instantiate forms
    form = TherapistProfileForm(instance=profile)
    formset = AvailabilityFormSet(
        queryset=Availability.objects.filter(therapist=profile)
    )

    if request.method == 'POST':
        form = TherapistProfileForm(request.POST, request.FILES, instance=profile)
        formset = AvailabilityFormSet(
            request.POST, 
            queryset=Availability.objects.filter(therapist=profile)
        )

        if form.is_valid() and formset.is_valid():
            # Save profile
            form.save()

            # Save each availability entry
            for availability_form in formset:
                availability = availability_form.save(commit=False)
                availability.therapist = profile
                if availability_form.cleaned_data.get('DELETE'):
                    availability.delete()
                else:
                    availability.save()

            return redirect('therapist_profile')  # Redirect to the profile view

    return render(request, 'therapist_profiles/therapist_profile_form.html', {
        'form': form,
        'formset': formset,
    })
    
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

