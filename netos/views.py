from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-
# netos/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from .models import Device


# index

def index(request):
    """
    Index page
    """
    # return HttpResponse("Aplikacja netOS!")
    return render(request, 'netos/index.html')


# login

def loginPage(request):
    """
    User login page
    """
    from django.contrib.auth.forms import AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # messages.success(request, "Zostales zalogowany!")
            return redirect(reverse('netos:index'))

    context = {'form': AuthenticationForm()}
    return render(request, 'netos/loginWeb.html', context)


# logout

def logoutPage(request):
    """
    User logout page
    """
    logout(request)
    # messages.info(request, "Zostałeś wylogowany!")
    return redirect(reverse('netos:index'))

def devicesPage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    zapytanie = Device.objects.all().order_by('name')
    dane = {'zapytanie' : zapytanie}
    return render(request, 'netos/devices.html', dane)

def addDevicePage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    return render(request, 'netos/addDevice.html')

def removeDevicePage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    return render(request, 'netos/removeDevice.html')

def helpPage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    return render(request, 'netos/help.html')
def ip_reservationPage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    return render(request, 'netos/ip_reservation.html')
def cpuPage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    return render(request, 'netos/cpu.html')
def memory_usagePage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    return render(request, 'netos/memory_usage.html')
def disk_usagePage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    return render(request, 'netos/disk_usage.html')
def networkPage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    return render(request, 'netos/network.html')
