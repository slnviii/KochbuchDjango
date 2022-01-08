from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):   # Kategorieklasse für Rezepte
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name  # Echter name statt "Objekt"


class Zutat(models.Model):    # Zutatenklasse
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
    author = models.CharField('Author', max_length=10, null=True, blank=True)
    def __str__(self):
        return self.title   # bild titel statt "objekt"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('Avatar', upload_to="avatars")
