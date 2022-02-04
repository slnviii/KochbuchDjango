from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect # get_object_or_404 hinzugefügt
from django import forms
from django.urls import reverse_lazy
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
import random
from .forms import UpdateProfileForm, CommentForm
from . import models
from django.conf import settings
from django.db.models.signals import post_save
from .models import Profile, Comment, Recipe
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.


class RecipeForm(forms.ModelForm):
    """Klasse zur Formularerstellung."""
    class Meta:
        model = models.Recipe
        exclude = []


class overview(ListView):      # Startseite
    model = Recipe
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(overview, self).get_context_data(*args, **kwargs)
        recipe_dict = []
        all_recipes = list(Recipe.objects.all())
        context["recipes"] = models.Recipe.objects.all()
        context["random_recipe"] = random.choice(all_recipes)

        return context

def random_recipe(request):
    all_recipes = list(Recipe.objects.all())
    rec = random.choice(all_recipes)
    return HttpResponse(rec)




@login_required()
def upload(request):

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():  # Formular überprüfen
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form.save_m2m()
            return HttpResponseRedirect('/')  # Umleitung
        else:
            print(form.errors)
    else:
        form = RecipeForm()  # leeres Formular
    return render(request, 'upload.html', dict(form=form))


def rezepte_main(request):
    all_categories = models.Category.objects.all()
    all_tags = models.Tag.objects.all()
    all_themes = models.Theme.objects.all()
    return render(request, 'rezepte_main.html', dict(categories=all_categories,tags=all_tags,themes=all_themes))


@login_required()
def profile_view(request):
    storage = messages.get_messages(request)
    all_recipes = models.Recipe.objects.all()

    return render(request, 'profile_page.html',  dict(recipes=all_recipes, message=storage))


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,"Successfully Changed Your Profile")
            return HttpResponseRedirect('/profile/')
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'edit_profile.html', {'profile_form': profile_form})

class ChangePasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('profile')


def AddFavorite(request, pk):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    added = False
    if recipe.favorite.filter(id=request.user.id).exists():
        recipe.favorite.remove(request.user)
        added = False
    else:
        recipe.favorite.add(request.user)
        added = True
    return HttpResponseRedirect(reverse('recipe', args=[str(pk)]))

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('overview')
    def form_valid(self,form):
        form.instance.recipe_id = self.kwargs['pk']
        return super().form_valid(form)

class RecipeView(DetailView):      # Rezept darstellen
    model = Recipe
    template_name = 'display_recipe.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RecipeView, self).get_context_data(*args, **kwargs)
        current = get_object_or_404(Recipe, id=self.kwargs['pk'])
        total_favorites = current.total_favorites()  # recipe model function callen
        added = False
        if current.favorite.filter(id=self.request.user.id):        # ist schon favorit?
            added = True
        context["total_favorites"] = total_favorites
        context["added"] = added
        return context


class DeleteComment(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('overview')


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        recipes = Recipe.objects.filter(title__icontains=searched)
        return render(request, 'search.html', dict(searched=searched, recipes=recipes))
    else:
        return render(request, 'search.html', {})


class EditRecipeView(UpdateView):
    model = Recipe
    template_name = 'edit_recipe.html'
    fields = ['title','image', 'ingr', 'instr', 'kategorien','tags','thema', 'dauer', 'schwierigkeit']



def category(request, category_name):
    category = models.Category.objects.get(name=category_name)
    return render(request, 'category.html', dict(category=category))

def tag(request, tag_name):
    tag = models.Tag.objects.get(name=tag_name)
    return render(request, 'tag.html', dict(tag=tag))

def theme(request, theme_name):
    theme = models.Theme.objects.get(name=theme_name)
    return render(request, 'theme.html', dict(theme=theme))


def filter_form(request):
    all_categories = models.Category.objects.all()
    all_users = User.objects.all()
    return render(request, 'filter.html', dict(
        categories=all_categories,
        users=all_users,
    ))


def time(request):
    return HttpResponse(datetime.datetime.now().strftime("%H:%M:%S"))


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
