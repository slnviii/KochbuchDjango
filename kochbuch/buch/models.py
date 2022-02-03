from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Category(models.Model):   # Kategorieklasse für Rezepte
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name  # Echter name statt "Objekt"


class Theme(models.Model):   #Themenklasse für Rezepte
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name  # Echter name statt "Objekt"


class Tag(models.Model):   #Tagklasse für Rezepte
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
    thema = models.ForeignKey(Theme, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, null=True)
    #zutaten = models.ManyToManyField(Zutat)  # Rezept hat mehrere Zutaten
    author = models.ForeignKey(User, to_field="username", db_column="username", on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ManyToManyField('Comment', related_query_name='comment', blank=True, null=True)
    dauer = models.IntegerField('Dauer',default="30")
    schwierigkeit = models.CharField(max_length=15, choices=(('superleicht','Sehr leicht'),('leicht','Leicht'),('mittel','Mittel'),('schwer','Schwer')),default='leicht')
    favorite = models.ManyToManyField(User, related_name='rezepte',null=True, blank=True)
    #bewertet = models.ManyToManyField('Rating', null=True)


    def total_favorites(self):
        return self.favorite.count()


    def __str__(self):
        return self.title   # bild titel statt "objekt"


    def get_absolute_url(self):
        return reverse('recipe', args=str(self.id))

# class Rating(models.Model):
#     bewertung = models.IntegerField(max_length=1, choices=(('0', '0 Sterne'),('1', '1 Stern'),('2', '2 Sterne'),('3', '3 Sterne'),('4', '4 Sterne'),('5', '5 Sterne')),default="0")



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField('Avatar', upload_to="avatars",default='avatars/default-avatar.jpg')
    favorite = models.ManyToManyField(Recipe, null=True)
    bio = models.TextField(null=True)
    def __str__(self):
        return str(self.user)



class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField('Author', max_length=100, null=True, blank=True)
    body = models.TextField('Kommentar:')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.recipe)