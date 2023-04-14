from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

#TRIBE------------------
class Tribe(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tribe, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    @classmethod
    def all(cls):
        return list(cls.objects.all())

#SQUAD--------------------
class Squad(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Squad, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detalhes_squad', kwargs={'tribe_slug': self.tribe.slug, 'squad_slug': self.slug})

    def __str__(self):
        return self.name


#-------------------#
#-PERFIL DO USUÁRIO-#
#-------------------#
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
    squads = models.ManyToManyField(Squad, blank=True, related_name="member")
#
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
#
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
#
    def __str__(self):
        return self.user.username