from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    email = models.EmailField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
    
    def __str__(self):
        return self.user.username
    
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
    