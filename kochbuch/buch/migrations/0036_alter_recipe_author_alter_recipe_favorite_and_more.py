# Generated by Django 4.0.1 on 2022-01-24 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buch', '0035_remove_zutat_menge_remove_zutat_recipe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(blank=True, db_column='username', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='favorite',
            field=models.ManyToManyField(blank=True, null=True, related_name='rezepte', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='buch.Tag'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='thema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buch.theme'),
        ),
    ]
