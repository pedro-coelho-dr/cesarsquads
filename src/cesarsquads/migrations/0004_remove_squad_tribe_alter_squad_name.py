# Generated by Django 4.2 on 2023-04-12 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cesarsquads', '0003_alter_tribe_name_alter_tribe_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squad',
            name='tribe',
        ),
        migrations.AlterField(
            model_name='squad',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
