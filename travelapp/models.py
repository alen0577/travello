from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pictures')
    des = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Blog(models.Model):
    date = models.DateField(null=True)
    img = models.ImageField(upload_to='pictures')
    title = models.CharField(max_length=250)
    cat = models.CharField(max_length=250)
    des = models.TextField()
