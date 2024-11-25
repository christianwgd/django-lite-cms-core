# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout


def index(request):
    return render(request, 'index.html', {})


def log_off(request):
    logout(request)
    return redirect(reverse('home'))
