# Generated by Django 4.1.7 on 2023-03-27 07:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('OnlyTrucks', '0012_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='camion',
            name='Publicado_el',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='remolques',
            name='Publicado_el',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
