from django.db import models

# Create your models here.
class place(models.Model):
    name= models.CharField(max_length=100)
    img=models.ImageField(upload_to='images')
    desc= models.TextField(max_length=200)
    price= models.IntegerField()
    offer=models.BooleanField(default=False)

class blog(models.Model):
    img=models.ImageField(upload_to='images')
    date=models.IntegerField()
    month=models.CharField(max_length=100)
    title=models.TextField(max_length=300)
    caption=models.TextField(max_length=300)
    desc=models.TextField(max_length=400)
