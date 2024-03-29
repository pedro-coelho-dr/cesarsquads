# Generated by Django 4.2 on 2023-04-14 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cesarsquads', '0005_tribe_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='slug',
            field=models.SlugField(default=2, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squad',
            name='tribe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cesarsquads.tribe'),
            preserve_default=False,
        ),
    ]
