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
    
class Tribo(models.Model):
    nameExibitionTribe = models.CharField(max_length=100)
    descriptionTribe = models.CharField(max_length=300)
    photoTribe = models.ImageField(upload_to='tribe_images', default='')
    maxSquads = models.DecimalField(blank=True)
    maxUserSquads = models.DecimalField(blank=True)
    
    def __str__(self):
        return self.nameExibitionTribe
    
class Squad(models.Model):
    nameExibitionSquad = models.CharField(max_length=100)
    descriptionSquad = models.CharField(max_length=300)
    photoSquad = models.ImageField(upload_to='squad_images', default='')
    maxUsers = models.DecimalField(blank=True)
    
    def __str__(self):
        return self.nameExibitionSquad
    