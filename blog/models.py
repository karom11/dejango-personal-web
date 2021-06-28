from django.db import models

# Create your models here.

class Post(models.Model):
    sidetitles= models.CharField(max_length=100)
    imge = models.ImageField(upload_to'posts/')
    Suspension = models.TextField(max_length=300)
    text 
    