from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    gmail = models.CharField(max_length=100,blank=True,null=True)
    subject = models.CharField(max_length=100,blank=True,null=True)
    message = models.CharField(max_length=100,blank=True,null=True)
