# Generated by Django 4.2 on 2023-04-06 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
                ('password2', models.CharField(max_length=12)),
                ('bio', models.CharField(max_length=500)),
                ('photo', models.ImageField(default='', upload_to='profile_images')),
            ],
        ),
    ]
