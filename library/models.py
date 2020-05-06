from django.db import models

# Create your models here.

class Books(models.Model):
    Title = models.CharField(max_length=500)
    Author = models.CharField(max_length=100)
    Desc = models.CharField(max_length=500)
    Category= models.CharField(max_length=50)
    AgeCategory= models.CharField(max_length=50)
    NOOfPages= models.IntegerField()
    Img = models.ImageField(upload_to='pics')
    IsAvailable = models.BooleanField(default='false')
