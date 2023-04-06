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
    
    # sfsfsfsf