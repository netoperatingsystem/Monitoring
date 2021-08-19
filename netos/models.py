from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    address_ip = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Labipaddress(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    address_ip = models.CharField(max_length=15)
    address_mac = models.CharField(max_length=12)
    def __str__(self):
        return self.name + " - " + self.address_ip + " - " + "connected to" + " - " + self.device.name