from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TherapistProfileForm, AvailabilityForm
from .models import TherapistProfile, Availability
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from django.contrib import messages

# Index view
def index(request):
    return render(request, 'therapist_profiles/index.html')

@login_required
def create_or_update_profile(request):
    # Get or create the therapist's profile
    profile, created = TherapistProfile.objects.get_or_create(user=request.user)

    # Define the formset for Availability
    AvailabilityFormSet = modelformset_factory(
        Availability,
        form=AvailabilityForm,
        extra=1,
        can_delete=True
    )

    if request.method == 'POST':
        # Bind form and formset data
        form = TherapistProfileForm(request.POST, request.FILES, instance=profile)
        formset = AvailabilityFormSet(request.POST, queryset=Availability.objects.filter(therapist=profile))

        if form.is_valid() and formset.is_valid():
            # Save the profile
            form.save()

            # Process the formset
            for availability_form in formset:
                if availability_form.cleaned_data.get('DELETE'):
                    if availability_form.instance.pk:  # Delete the record if it exists
                        availability_form.instance.delete()
                else:
                    availability = availability_form.save(commit=False)
                    availability.therapist = profile  # Assign the therapist to the availability
                    availability.save()

            return redirect('therapist_profile')

    else:
        # Initialize form and formset for GET requests
        form = TherapistProfileForm(instance=profile)
        formset = AvailabilityFormSet(queryset=Availability.objects.filter(therapist=profile))

    return render(request, 'therapist_profiles/therapist_profile_form.html', {
        'form': form,
        'formset': formset,
    })

@login_required
def view_profile(request):
    profile, created = TherapistProfile.objects.get_or_create(user=request.user)
    return render(request, 'therapist_profiles/therapist_profile.html', {'profile': profile})

@login_required
def view_profile_by_id(request, user_id):
    profile = get_object_or_404(TherapistProfile, user_id=user_id)
    return render(request, 'therapist_profiles/therapist_profile.html', {'profile': profile})

@login_required
def view_profile_by_username(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = TherapistProfile.objects.get_or_create(user=user)
    return render(request, 'therapist_profiles/therapist_profile.html', {'profile': profile})

def therapist_profiles(request):
    # Fetch all therapist profiles
    profiles = TherapistProfile.objects.all()

    # Pass the logged-in user and all profiles to the template
    return render(request, 'therapist_profiles/therapist_profile.html', {
        'profiles': profiles,
        'logged_in_user': request.user,  # Pass logged-in user to determine edit button visibility
    })