from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=45, null=True, blank=True)
    email = models.CharField(max_length=45, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(default="profiles/user-default.png", null=True, blank=True, upload_to='profiles/')
    social_media = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)
    

class Device(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    model = models.CharField(max_length=55, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    purchased = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.model)
    

