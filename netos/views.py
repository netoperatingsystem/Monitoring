from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-
# netos/views.py
import pandas
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from .models import Device
from .models import Labipaddress
from .models import Category
from .forms import NowyLabipaddressForm


# index

def index(request):
    """
    Index page
    """
    # return HttpResponse("Aplikacja netOS!")
    labip = Device.objects.all().order_by('name')
    data_ip = {'Device': labip}
    return render(request, 'netos/index.html', data_ip)
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


def devicesPageid(request):

    try:
        device_id = Device.objects.filter(pk=id)
    except:
        device_id = None

    if device_id:
        ip_address_raw = str(device_id.address_ip)

    ip_address = ip_address_raw.replace(".", "_")

    if_info_file = "app/Monitoring/netos/snmp-ifInfo-" + ip_address

    import csv

    results = []
    with open(if_info_file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            results.append(row)

    return render(request, 'netos/removeIpAddress.html', results)

def helpPage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    return render(request, 'netos/help.html')


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
    return render(request, 'netos/cpu.html')


def memory_usagePage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    labip = Device.objects.all().order_by('name')
    data_ip = {'Device': labip}
    return render(request, 'netos/memory_usage.html', data_ip)
    return render(request, 'netos/memory_usage.html')


def disk_usagePage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    labip = Device.objects.all().order_by('name')
    data_ip = {'Device': labip}
    return render(request, 'netos/disk_usage.html', data_ip)
    return render(request, 'netos/disk_usage.html')


def networkPage(request):
    """
    Devices list page
    """
    # return HttpResponse("Aplikacja netOS!")
    labip = Device.objects.all().order_by('name')
    data_ip = {'Device': labip}
    return render(request, 'netos/network.html', data_ip)
    return render(request, 'netos/network.html')

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
        "form" : nowy_form
    }

    return render(request, 'netos/addIpAddress.html', context)

def removeIpAddressPage(request):
    result = Labipaddress.objects.all().order_by('name')
    result_name_IpAddress = Labipaddress.objects.all().order_by('name')
    result_addressIP_IpAddress = Labipaddress.objects.all().order_by('address_ip')
    result_address_mac = Labipaddress.objects.all().order_by('address_mac')
    result_ip = {'Labipaddress': result, 'Labipaddress': result_name_IpAddress, 'Labipaddress': result_addressIP_IpAddress,'Labipaddress': result_address_mac}
    return render(request, 'netos/removeIpAddress.html', result_ip)



