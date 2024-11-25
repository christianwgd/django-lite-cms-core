# -*- coding: utf-8 -*-
from django.db import models

from lite_cms_core.models import BaseEntity


class BaseItem(BaseEntity):
    """
    Objects for testing the BaseEntity model.
    """

    string_property = models.CharField(max_length=20)