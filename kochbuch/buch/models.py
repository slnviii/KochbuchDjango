from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):   # Kategorieklasse für Rezepte
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name  # Echter name statt "Objekt"


class Zutat(models.Model):    # Zutatenklasse für später
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name    # echter name statt "objekt"


class Recipe(models.Model):
    title = models.CharField('Titel', max_length=200)
    image = models.ImageField('Bild')
    ingr = models.TextField('Zutaten', max_length=500)
    instr = models.TextField('Zubereitung', max_length=10000)
    kategorien = models.ManyToManyField(Category)  # Rezept kann mehrere Kategorien haben und umgekehrt
    #  zutaten = models.ManyToManyField(Zutat)  # Rezept hat mehrere Zutaten
    author = models.ForeignKey(User, to_field="username", db_column="username", on_delete=models.CASCADE)
    comment = models.ManyToManyField('Comment', related_query_name='comment', blank=True)
    def __str__(self):
        return self.title   # bild titel statt "objekt"




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('Avatar', upload_to="avatars")
    favorites = models.ManyToManyField(Recipe, related_name='favorites', null=True, blank=True)

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField('Author', max_length=10, null=True, blank=True)
    body = models.TextField('Kommentar:')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.recipe)