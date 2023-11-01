
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

def signup_view(request):
    # Handle user sign up logic here
    pass


def login_view(request):
    return render(request, 'login.html')

@login_required
def profile_view(request):
    user_profile = request.user
    if request.method == "POST":
        # Assuming a ProfileForm is defined to handle profile updates
        form = ProfileForm(request.POST, request.FILES, 
                           
  instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile_view')
        else:
            messages.error(request, "There was an error updating your profile.")
    else:
        form = ProfileForm(instance=user_profile)
    
    context = {
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'user_profiles/profile.html', context)
