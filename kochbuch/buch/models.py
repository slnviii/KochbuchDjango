from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Recipe(models.Model):
    title = models.CharField('Titel', max_length=200)
    image = models.ImageField('Bild')
    ingr = models.TextField('Zutaten', max_length=500)
    instr = models.TextField('Zubereitung', max_length=10000)

