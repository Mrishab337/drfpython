from django.db import models

class Businessregister(models.Model):
    business_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    workspacename = models.CharField(max_length=100, unique=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.business_name
