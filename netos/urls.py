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
    # url(r'^<str:room_name>/$', views.room, name='room'),
]