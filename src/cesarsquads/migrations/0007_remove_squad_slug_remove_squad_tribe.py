# Generated by Django 4.2 on 2023-04-16 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cesarsquads', '0006_squad_slug_squad_tribe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squad',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='squad',
            name='tribe',
        ),
    ]
