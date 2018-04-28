from django.db import models
from django.contrib.auth.models import User

class RegUser(models.Model):
    """
    This is the User registeration table of our project.
    The following are the columns of the table.
    The fields to be set are name, email, password 
    """
    #user = models.OneToOneField(User)
    
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.email


class Vasp(models.Model):
    VAS_Type = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.email_id

# Create your models here.
