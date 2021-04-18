from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    address_ip = models.CharField(max_length=15)
    def __str__(self):
        return self.name