# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout
from django.views.generic import DetailView

from lite_cms_core_sample.models import SluggedItem


def index(request):
    return render(request, 'index.html', {})


class SluggedItemDetailView(DetailView):
    model = SluggedItem