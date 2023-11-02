from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib import messages
from .forms import UserRegisterForm


def signup_view(request):
    # Firebase will handle sign up, so this view is just to render the template
    return render(request, 'user_profiles/signup.html')

def login_view(request):
    # Firebase will handle login, so this view is just to render the template
    return render(request, 'user_profiles/login.html')
def profile_view(request):
    user_profile = request.user
    # Assuming a ProfileForm is defined to handle profile updates
    # Make sure to import or define it
    form = ProfileForm(instance=user_profile)  # Initialize it outside the POST check for now

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile_view')
        else:
            messages.error(request, "There was an error updating your profile.")

    context = {
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'user_profiles/profile.html', context)
