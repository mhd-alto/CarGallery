from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField



class Company(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=256)
    adderss = models.CharField(max_length=256)
    company_phonenumber = PhoneNumberField()
    statement = models.ImageField(upload_to='statement_Company/')
    payment_note_image = models.ImageField(upload_to='payment_note_image_Company/')
    company_services = models.TextField(max_length=1024)
    company_logo = models.ImageField(upload_to='company_logo/')
    is_active = models.BooleanField(null=True,blank=True,default=False)
    

    def __str__(self):
        return self.company_name

