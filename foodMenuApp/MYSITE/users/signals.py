from django.db.models.signals import post_save #a signal which decides what will happen after save
from django.contrib.auth.models import User # this may be a sender will confirm latter
from django.dispatch import receiver #recieve the sent signal
from .models import Profile

#when reciver recieves a signal it will create a profile

#sender the one who sent the signal
#instance the form data
#created returns a boolean value yes created user no not created dont make profile
#how exactly do we know that the user profile is created? -> post_save
@receiver(post_save,sender=User)
def build_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        
# going to save profile
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
    
#dont forget to configure the apps.py file    