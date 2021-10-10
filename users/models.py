from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from random import randint
from django.conf import settings
# Create your models here.

def split_ext(file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_path(instance, filepath):
    name, ext = split_ext(filepath)
    new_name  =  randint(0, 999999999)
    final_path = f"avatars/{instance.user.username}/{instance.id}/{new_name}{ext}"
    return final_path

class CustomUserModel(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return super().username

class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='avatars/default.png', upload_to=upload_path)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        if self.first_name == '' or self.last_name == '':
            return f'{self.user.username} Profile\'s'
        return f'{self.first_name} {self.last_name}'