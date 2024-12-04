from django.db import models

# Create your models here.

class Businessregister(models.Model):
    business_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    workspacename=models.CharField(max_length=100)
    