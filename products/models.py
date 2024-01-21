from django.db import models
from django.conf import settings
from djmoney.models.fields import MoneyField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from account.models import Company

class Brand(models.Model):
    brand = models.CharField(max_length=256)

    def __str__(self):
        return self.brand

class Color(models.Model):
    color = models.CharField(max_length=256)

    def __str__(self):
        return self.color

class Car(models.Model):
    author = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='product_author')
    title = models.CharField(max_length=256)
    main_image = models.ImageField(upload_to='products/')
    description = models.TextField(max_length=1024)
    price = MoneyField(x    )
    brand = models.ForeignKey(Brand,on_delete=models.SET_NULL,null=True,blank=True)
    color = models.ForeignKey(Color,on_delete=models.SET_NULL,null=True,blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='likes',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
class CarComment(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    text = models.TextField(max_length=512)

    def __str__(self):
        return self.car.title


# class CarLike(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     car = models.ForeignKey(Car,on_delete=models.CASCADE)


#     def __str__(self):
#         return str(self.user)+"like on"+str(self.car)


class CarPart(models.Model):
    author = models.ForeignKey(Company,on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(max_length=1024)
    price = MoneyField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand,on_delete=models.SET_NULL,null=True,blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='parts_likes',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class CarPartComment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    carPart = models.ForeignKey(CarPart,on_delete=models.CASCADE)
    text = models.TextField(max_length=512)

    def __str__(self):
        return self.author

class Offers(models.Model):
    author = models.ForeignKey(Company,on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(max_length=1024)
    price = MoneyField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class OffersComment(models.Model):
    Offer = models.ForeignKey(Offers,on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    text = models.TextField(max_length=512)

    def __str__(self):
        return self.author