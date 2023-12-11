from django.forms import ModelForm
from . models import Photos

class PhotoGraphyForm(ModelForm):
    class Meta:
        model = Photos
        fields = ['name', 'description', 'location', 'image']