# Generated by Django 4.2 on 2023-05-10 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cesarsquads', '0008_squad_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='tribe',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='cesarsquads.tribe'),
            preserve_default=False,
        ),
    ]
