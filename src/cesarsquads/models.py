from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    password2 = models.CharField(max_length=12)
    bio = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='profile_images',default='')
    
    def __str__(self):
        return self.name
    
class Tribe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='tribe_images', default='')
    max_squads = models.IntegerField(blank=True)
    max_user_squad = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.name
    
class Squad(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='squad_images', default='')
    max_users = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.name
    