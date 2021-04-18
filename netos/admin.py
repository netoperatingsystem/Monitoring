# Register your models here.

from django.contrib import admin
from netos import models
from .models import Device

admin.site.register(Device)