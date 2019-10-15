from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import PIL
from django.urls import reverse



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(default = 'default.jpg', upload_to ='profile_pics')
    bio = models.CharField(max_length=280, blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username}\'s Profile'