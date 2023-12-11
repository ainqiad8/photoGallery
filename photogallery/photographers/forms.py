from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile, Device

from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

        labels = {
            'first_name': "Name",
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'bio', 'profile_image', 'social_media']



class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class":"input"})