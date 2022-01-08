# Generated by Django 4.0.1 on 2022-01-08 00:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buch', '0003_alter_recipe_instr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='instr',
            field=models.TextField(max_length=10000, verbose_name='Zubereitung'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='avatars', verbose_name='Avatar')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
