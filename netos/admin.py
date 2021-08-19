# Register your models here.

from django.contrib import admin
from netos import models
from .models import Device
from .models import Labipaddress

admin.site.register(Device)
admin.site.register(Labipaddress)