from django import forms
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
        exclude = ['user']


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            # profile_form.data.user = form.data.user   # wie verknüpfen?
            profile_form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'registration/register.html', dict(form=form, profile_form=profile_form))
