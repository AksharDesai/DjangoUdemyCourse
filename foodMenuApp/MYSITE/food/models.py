from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
      
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default='https://t3.ftcdn.net/jpg/05/04/28/96/360_F_504289605_zehJiK0tCuZLP2MdfFBpcJdOVxKLnXg1.jpg')
 
    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse("food:item_detail", kwargs={"item_id": self.pk})#passing an primary key too becuase we are going to detail page
    