from django import forms
from django.contrib.auth import authenticate, login as login_user
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
# Create your views here.
from buch import models


def login(request):
    pass


def logout(request):
    pass


class ProfileForm(forms.ModelForm):
    """Klasse zur Formularerstellung."""
    class Meta:
        model = models.Profile
        exclude = ['user', 'favorite']


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
       # profile_form = ProfileForm(request.POST)
        if form.is_valid():  # and profile_form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user:
                login_user(request, user)
                return redirect('/')
            # profile_form.data.user = form.data.user   # wie verknüpfen?
           # profile_form.save()

    else:
        form = UserCreationForm()
        # profile_form = ProfileForm()
    return render(request, 'registration/register.html', dict(form=form))  # , profile_form=profile_form))
