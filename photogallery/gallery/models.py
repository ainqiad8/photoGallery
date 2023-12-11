from django.db import models
from photographers.models import Profile
# Create your models here.

class Photos(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=False, blank= False)
    description = models.TextField()
    image = models.ImageField(default='default.jpg', null=True, blank=True)
    device = models.CharField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    