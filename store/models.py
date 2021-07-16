from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images')
    
    
    def __str__(self):
        return self.name
    def __int__(self):
        return self.price

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
