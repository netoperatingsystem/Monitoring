# -*- coding: utf-8 -*-
# netos/urls.py

from django.conf.urls import url
from django.urls import path
from netos.views import *


from . import views             # import of application views

app_name = 'netos'              # application namespace
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.loginPage, name='login'),
    url(r'^logout/$', views.logoutPage, name='logout'),
    url(r'^devices/$', views.devicesPage, name='devices'),
    path('devices/<id>/', devicesPageid, name='devicesPageId'),
    url(r'^ip_reservation/addIpAddress/$', views.addIpAddressPage, name='addIpAddress'),
    url(r'^ip_reservation/$', views.ip_reservationPage, name='ip_reservation'),
    url(r'^about/$', views.aboutPage, name='about'),
    url(r'^cpu/$', views.cpuPage, name='cpu'),
    url(r'^memory_usage/$', views.memory_usagePage, name='memory_usage'),
    url(r'^disk_usage/$', views.disk_usagePage, name='disk_usage'),
]
