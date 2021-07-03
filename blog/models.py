from django.db import models
from _datetime import timezone


# Create your models here.

class home(models.Model):
    sidetitles = models.CharField(max_length=100)
    imge =models.ImageField(upload_to='home/')
    Suspension =models.TextField(max_length=300)
    



   

class About(models.Model):
    imge =models.ImageField(upload_to='About/') 
    titel = models.CharField(max_length=100)
    subtitle =models.TextField(max_length=300)
    comint =models.TextField(max_length=3000)




class post(models.Model):
    imge =models.ImageField(upload_to='posts/')
    titel = models.CharField(max_length=100)
    subtitle =models.TextField(max_length=300)