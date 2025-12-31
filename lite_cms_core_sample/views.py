from django.shortcuts import render
from django.views.generic import DetailView

from lite_cms_core_sample.models import SluggedItem, ContentItem, BaseItem


def index(request):
    return render(request, 'index.html', {})

class BaseItemDetailView(DetailView):
    model = BaseItem

class SluggedItemDetailView(DetailView):
    model = SluggedItem

class ContentItemDetailView(DetailView):
    model = ContentItem
