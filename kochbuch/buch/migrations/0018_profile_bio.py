# Generated by Django 4.0.1 on 2022-01-22 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buch', '0017_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
