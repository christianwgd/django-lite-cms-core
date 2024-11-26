# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse

from lite_cms_core.models import BaseEntity, SluggedMixin, ContentFieldMixin


class BaseItem(BaseEntity):
    """
    Objects for testing the BaseEntity model.
    """

    search_fields = {"title"}

    def get_absolute_url(self):
        return reverse('base-item-detail', kwargs={'pk': self.pk})


class SluggedItem(SluggedMixin, BaseItem):
    """
    Objects for testing the SluggedItem model.
    """

    def get_absolute_url(self):
        return reverse('slugged-item-detail', args=[str(self.slug)])


class SluggedItemFromName(SluggedMixin, BaseItem):
    """
    Objects for testing the SluggedItem model.
    """

    name = models.CharField(max_length=100)

    def get_slug(self, attr=None):
        return super().get_slug(attr="name")


class ContentItem(ContentFieldMixin, SluggedMixin, BaseItem):
    """
    Objects for testing the search views.
    """

    search_fields = {"title", "content"}

    def get_absolute_url(self):
        return reverse('content-item-detail', args=[str(self.slug)])
