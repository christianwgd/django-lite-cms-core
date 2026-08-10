from django.shortcuts import render
from django.views.generic import DetailView

from lite_cms_core.models import PreventUnpublishedAccessDetailView
from lite_cms_core_sample.models import BaseItem, ContentItem, SluggedItem


def index(request):
    return render(request, "index.html", {})

class BaseItemDetailView(PreventUnpublishedAccessDetailView):
    model = BaseItem

class SluggedItemDetailView(DetailView):
    model = SluggedItem

class ContentItemDetailView(DetailView):
    model = ContentItem
