from django.contrib.auth.models import User
from django import forms
from user.models import Profile
def validate_unique_user(error_message, **criteria):
    existent_user = User.objects.filter(**criteria)
    if existent_user:
        raise forms.ValidationError(error_message)

class SignupForm(forms.ModelForm):

    username = forms.CharField(max_length=10,widget=forms.TextInput({
        'placdholder': 'User name' }))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput({
         'placdholder': 'First name' }))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput({
        'placdholder': 'Last name' }))
    email = forms.EmailField(widget=forms.EmailInput({
        'placdholder': 'Email', 'placdholder': 'Email' }))
    password = forms.CharField(min_length=6, max_length=20,widget=forms.PasswordInput
              ({'placdholder': 'Password' }))
    repeat_password = forms.CharField(min_length=6, max_length=20,widget=forms.PasswordInput ({'placdholder': 'Repeat password' }))

    def clean_username(self):
        username = self.cleaned_data['username']
        validate_unique_user(error_message='* Username already in use', username=username)
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        validate_unique_user(error_message='* Email already in use', email=email)
        return email

    def clean_repeat_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('repeat_password')
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password1

class UserEditForm(forms.ModelForm):
    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date', 'photo']
