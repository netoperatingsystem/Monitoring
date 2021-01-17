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


def index(request):
    """Strona główna aplikacji."""
    #return HttpResponse("Aplikacja netOS!")
    return render(request, 'netos/index.html')
def loginPage(request):
    """user login"""
    from django.contrib.auth.forms import AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Zostales zalogowany!")
            return redirect(reverse('netos:index'))

    kontekst = {'form': AuthenticationForm()}
    return render(request, 'netos/loginWeb.html', kontekst)


def logoutPage(request):
    """user logout"""
    logout(request)
    messages.info(request, "Zostałeś wylogowany!")
    return redirect(reverse('netos:index'))
