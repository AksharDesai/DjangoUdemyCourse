from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField( max_length=50)
    image = models.ImageField( upload_to='profile_pictures', max_length=None , default='profile.jpg',null=False,blank=False)
    def __str__(self):
        return self.location