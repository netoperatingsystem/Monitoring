# -*- coding: utf-8 -*-
# netos/urls.py

from django.conf.urls import url
from . import views  # import of application views


app_name = 'netos'  # application namespace
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.loginPage, name='login'),
    url(r'^logout/$', views.logoutPage, name='logout'),
]