# -*- coding: utf-8 -*-
# netos/urls.py

from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from . import views             # import of application views

app_name = 'netos'              # application namespace
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.loginPage, name='login'),
    url(r'^logout/$', views.logoutPage, name='logout'),
    url(r'^devices/$', views.devicesPage, name='devices'),
    url(r'^devices/addDevice', views.addDevicePage, name='addDevice'),
    url(r'^devices/removeDevice', views.removeDevicePage, name='removeDevice'),
    url(r'^ip_reservation/$', views.ip_reservationPage, name='ip_reservation'),
    url(r'^help/$', views.helpPage, name='help'),
    url(r'^cpu', views.cpuPage, name='cpu'),
    url(r'^memory_usage', views.memory_usagePage, name='memory_usage'),
    url(r'^disk_usage', views.disk_usagePage, name='disk_usage'),
    url(r'^network', views.networkPage, name='network'),

    # url(r'^<str:room_name>/$', views.room, name='room'),
]