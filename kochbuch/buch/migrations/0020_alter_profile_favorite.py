# Generated by Django 4.0.1 on 2022-01-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buch', '0019_rename_favorites_profile_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorite',
            field=models.ManyToManyField(null=True, to='buch.Recipe'),
        ),
    ]
