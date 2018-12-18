from django.contrib import auth
from django.db import models
from django.utils import timezone
#from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey

'''
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
'''
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.PROTECT)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    type_option = (
        ('interior designer','interior designer'),
        ('architect Engineers' , 'architect Engineers'),
        ('Valuation services' , 'Valuation services'),
    )
    type = models.CharField(max_length=30, choices=type_option, default='Valuation services')
    def __str__(self):

        return self.user.username



class Products(models.Model):
    user = UserForeignKey(auto_user_add=True, verbose_name="The user that is automatically assigned", related_name="mymodels")
    Area_Choices = (
        ('mustafa town', 'mustafa town'),
        ('johar town', 'johar town'),
        ('iqbal town', 'iqbal town'),
        ('defence', 'defence'),
    )
    select_option = (
        ('yes','yes'),('no','no')
    )
    status_option = (
        ('sale','sale'),
        ('rent' , 'rent')
    )
    location = models.CharField(max_length=30, choices=Area_Choices, default='mustafa_town')
    propertyTitle = models.CharField(max_length=200)
    description = models.CharField(max_length=20000 )
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=status_option, default='sale')
    price = models.CharField(max_length=100)
    Rooms  = models.IntegerField()
    BathRooms  = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    postalCode = models.IntegerField()
    buildingAge = models.CharField(max_length=100)
    freeParking = models.CharField(max_length=30, choices=select_option, default='yes')
    swimmingPool = models.CharField(max_length=30, choices=select_option, default='yes')
    airCondition = models.CharField(max_length=30, choices=select_option, default='yes')
    sqft_Measurement = models.CharField(max_length=100)
    contactName =  models.CharField(max_length=100)
    contactEmail = models.CharField(max_length=100)
    contactPhone = models.CharField(max_length=100)
    def __str__(self):
        return self.propertyTitle + '-' + self.status +'-' + self.price + '-' + self.location  + '-' + self.contactName + '-' + self.contactEmail +'-' + self.contactPhone + '-' + self.city



class Localities(models.Model):
    #localities_user = UserForeignKey(auto_user_add=True, verbose_name="The user that is automatically assigned", related_name="mymodels")
    locations_choice = (
        ('mustafa town','mustafa town'),
        ('iqbal town','iqbal town'),
        ('johar town', 'johar town'),
        ('defence', 'defence'),
        ('defence', 'defence'),
        ('Awan town', 'Awan town'),
        ('Eden', 'Eden'),
        ('Wapda town', 'Wapda town'),
    )
    location = models.CharField(max_length=136, choices=locations_choice, default='johar town')
    rate_locality = models.IntegerField()
    rate_cleanliness = models.IntegerField()
    rate_security = models.IntegerField()
    rate_parks = models.IntegerField()
    playGrounds = models.IntegerField()
    description = models.CharField(max_length=20000 )
    uploaded_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location

class Contact(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=100)
    Message = models.CharField(max_length=10000)

    def __str__(self):
        return self.name
