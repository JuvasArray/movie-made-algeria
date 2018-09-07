from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from user.forms import SignupForm, UserEditForm, ProfileEditForm
from user.models import Profile

@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html', {})

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
            )
            user.save()
            # Create profile
            Profile.objects.create(user=user)
            return render(request, 'user/register_done.html', {})
    else:
        form = SignupForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES,)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfuly')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'user/edit.html', {'user_form': user_form, 'profile_form': profile_form})

