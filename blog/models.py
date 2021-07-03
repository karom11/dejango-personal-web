from django.db import models
from _datetime import timezone


# Create your models here.

class post(models.Model):
    sidetitles = models.CharField(max_length=100)
    imge =models.ImageField(upload_to='posts/')
    Suspension =models.TextField(max_length=300)
    



   
