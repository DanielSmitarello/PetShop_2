from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='user_profile')
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    mail = models.CharField(max_length = 30)
    pet_name= models.CharField(max_length = 30)
    profile_img = models.ImageField(upload_to='profile_image', null = True, blank=True)


    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuario'

    def __str__(self):
        return self.name