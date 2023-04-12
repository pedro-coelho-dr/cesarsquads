from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

#TRIBE
class Tribe(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
#   description = models.CharField(max_length=300)
#   photo = models.ImageField(upload_to='tribe_images', default='blank-profile-picture.png')
#   max_squads = models.IntegerField(blank=True)
#   max_user_squad = models.IntegerField(blank=True)
    def __str__(self):
        return self.name

#SQUAD
class Squad(models.Model):
    name = models.CharField(max_length=100)
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE, blank=True)
#   description = models.CharField(max_length=300)
#   photo = models.ImageField(upload_to='squad_images', default='blank-profile-picture.png')
#   max_users = models.IntegerField(blank=True)
    def __str__(self):
        return self.name

#PERFIL  DO USUÁRIO
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
    squads = models.ManyToManyField(Squad, blank=True, related_name="member")
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    def __str__(self):
        return self.user.username