from django.contrib.auth.models import User
from . models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


#@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user=instance
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user 
    if created == False:
        user.first_name = profile.name
        user.last_name = profile.name
        user.username=profile.username
        user.email = profile.email


#@receiver(post_delete, sender=Profile)
def deleteProfile(sender, instance, **kwagrs):
    user = instance.user
    user.delete()

post_delete.connect(deleteProfile, sender=Profile)
post_save.connect(updateUser, sender=Profile)
post_save.connect(createProfile, sender=User)