from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from . import models

# Create your views here.


class RecipeForm(forms.ModelForm):
    """Klasse zur Formularerstellung."""
    class Meta:
        model = models.Recipe
        exclude = []


def overview(request):
    all_recipes = models.Recipe.objects.all()
    return render(request, 'index.html', dict(recipes=all_recipes))


def upload(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():  # Formular überprüfen
            form.save()
            return HttpResponseRedirect('/')  # Umleitung
    else:
        form = RecipeForm()  # leeres Formular
    return render(request, 'upload.html', dict(form=form))
