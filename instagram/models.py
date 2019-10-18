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
            output_size = (152,152)
            img.thumbnail(output_size)
            img.save(self.pic.path)

    @classmethod
    def search_by_username(cls,search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles

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


    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')

    @classmethod
    def filterby_id(cls, image_by):
        images = cls.Objects.filter(image_by)
    



class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
