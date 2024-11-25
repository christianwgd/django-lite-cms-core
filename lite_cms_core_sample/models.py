# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from lite_cms_core.models import BaseEntity, SluggedMixin


class BaseItem(BaseEntity):
    """
    Objects for testing the BaseEntity model.
    """


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

    def get_slug(self):
        attr = "name"
        return slugify(getattr(self, attr, None) or self.name)
