from django.contrib import admin
from myFYP.models import  Products, Localities, Contact, UserProfileInfo, User
# admin.site.register(RegUser)
admin.site.register(UserProfileInfo)
admin.site.register(Products)
admin.site.register(Localities)
admin.site.register(Contact)
# Register your models here.
