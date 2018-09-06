from django.contrib.auth.models import User
from django.shortcuts import render

from user.forms import SignupForm

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
            return render(request, 'user/register_done.html', {})
    else:
        form = SignupForm()
    return render(request, 'user/register.html', {'form': form})
