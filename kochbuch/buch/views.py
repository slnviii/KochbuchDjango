from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from . import models
from django.conf import settings
from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.


class RecipeForm(forms.ModelForm):
    """Klasse zur Formularerstellung."""
    class Meta:
        model = models.Recipe
        exclude = []


def overview(request):
    all_recipes = models.Recipe.objects.all()
    return render(request, 'index.html', dict(recipes=all_recipes))

@login_required()
def upload(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():  # Formular überprüfen
            form.save()
            return HttpResponseRedirect('/')  # Umleitung
    else:
        form = RecipeForm()  # leeres Formular
    return render(request, 'upload.html', dict(form=form))


def rezepte_main(request):
    all_recipes = models.Recipe.objects.all()
    return render(request, 'rezepte_main.html', dict(recipes=all_recipes))


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
