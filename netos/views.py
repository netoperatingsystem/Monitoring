from collections import Counter

from django.contrib import messages
from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-
# netos/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse
from .models import Device
from .models import Labipaddress
from .forms import NowyLabipaddressForm

import csv

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
    devicesPageid = Device.objects.all().order_by('name')
    dane = {'devicesPageid': devicesPageid}
    return render(request, 'netos/devices.html', dane)


def devicesPageid(request, id):

    try:
        device_id = Device.objects.filter(pk=id).values_list('address_ip').first()
    except:
        device_id = None

    if device_id:
        ip_address_raw = device_id

    ip_address = str(ip_address_raw[0]).replace(".", "_")

    file_raw_name = "app/Monitoring/netos/snmp-ifInfo-" + ip_address
    if_info_file = file_raw_name + ".csv"

    results = []
    with open(if_info_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            results.append(row)

    dev_ip = ip_address_raw[0]
    context_ip = {"dev_ip": dev_ip,
                  "results": results}

    return render(request, 'netos/devices-single.html', context_ip)


def aboutPage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    return render(request, 'netos/about.html')


def ip_reservationPage(request):
    """
    IP list page
    """
    request_ip = Labipaddress.objects.all().order_by('address_ip')
    data_ip = {'request_ip': request_ip}
    return render(request, 'netos/ip_reservation.html', data_ip)


def cpuPage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    labip = Device.objects.all().order_by('name')
    data_ip = {'Device': labip}
    return render(request, 'netos/cpu.html', data_ip)


def memory_usagePage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    labip = Device.objects.all().order_by('name')
    data_ip = {'Device': labip}
    return render(request, 'netos/memory_usage.html', data_ip)


def disk_usagePage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    labip = Device.objects.all().order_by('name')
    data_ip = {'Device': labip}
    return render(request, 'netos/disk_usage.html', data_ip)


def addIpAddressPage(request):
    nowy_form = NowyLabipaddressForm()
    if request.method == "POST":
        nowy_form = NowyLabipaddressForm(request.POST)
        if nowy_form.is_valid():
            #now our data type in form are correct
            print(nowy_form.cleaned_data)
            Labipaddress.objects.create(**nowy_form.cleaned_data)
        else:
            print(nowy_form.errors)
    context = {
        "form": nowy_form
    }
    return render(request, 'netos/addIpAddress.html', context)
