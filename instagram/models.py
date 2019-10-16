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

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = PIL.Image.open(self.pic.path)

        if img.height > 300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.pic.path)

class Image(models.Model):
    image_post = models.ImageField( upload_to='posts')
    image_caption = models.TextField()
    image_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.image_caption

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        img = PIL.Image.open(self.image_post.path)

        # if img.height > 300 or img.width >300:
        #     output_size = (300,300)
        #     img(output_size)
        #     img.save(self.image_post.path,format='JPEG')

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')