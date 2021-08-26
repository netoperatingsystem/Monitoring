from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Device(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    address_ip = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Labipaddress(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    address_ip = models.CharField(max_length=15)
    address_mac = models.CharField(max_length=12)
    def __str__(self):
        return self.name + " - " + self.address_ip + " - " + "connected to" + " - " + self.device.name

    class Meta:
        verbose_name = "Labipaddress"
        verbose_name_plural = "Labipaddresses"
