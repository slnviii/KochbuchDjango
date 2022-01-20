from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404 # get_object_or_404 hinzugefügt
from django import forms
from . import models
from django.conf import settings
from django.db.models.signals import post_save
from .models import Profile, Comment
from django.contrib.auth.decorators import login_required
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
            form.instance.author = request.user  # aktiver user wird automatisch als author des rezepts festgesetzt
            form.save()
            return HttpResponseRedirect('/')  # Umleitung
    else:
        form = RecipeForm()  # leeres Formular
    return render(request, 'upload.html', dict(form=form))


def rezepte_main(request):
    all_categories = models.Category.objects.all()
    return render(request, 'rezepte_main.html', dict(categories=all_categories))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body')


def recipe(request, recipe_name):
    #  rec_name = request.GET['name']      # hier wird der name des rezepts abgefragt auf den man geklickt hat
    recipe = models.Recipe.objects.get(title=recipe_name)  # das geklickte rezept wird gleichgesetzt und als objekt abgespeichert
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():  # Formular überprüfen
            form.instance.author = request.user  # aktiver user wird automatisch als author des rezepts festgesetzt
            # Create Comment object but don't save to database yet
            form = form.save(commit=False)
            # Assign the current recipe to the comment
            form.recipe = recipe
            # Save the comment to the database
            form.save()
            return HttpResponseRedirect('/')  # Umleitung
    else:
        form = CommentForm()  # leeres Formular
    all_comments = models.Comment.objects.all()
    return render(request, 'display_recipe.html', dict(form=form, recipe=recipe, comments = all_comments))
   # return render(request, 'display_recipe.html', dict(recipe=recipe))  # recipe object wird übergeben (s. display_recipe wie benutzt)


def category(request, category_name):
    category = models.Category.objects.get(name=category_name)    # ähnlich recipe, aber verknüpft mit rezept über manytomany, s. models
    return render(request, 'category.html', dict(category=category))  # dict übergeben, wird anders abgefragt, s. category.html l.41


@login_required()
def favorites(request, userid):
    favorites = get_object_or_404(RecipeForm, userid=userid)
    if models.Recipe.favorites.filter(userid=request.user.id).exists():
        models.Recipe.favorites.remove(request.user)
    else:
        models.Recipe.favorites.add(request.user)
    return HttpResponseRedirect('favorites/')



def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
