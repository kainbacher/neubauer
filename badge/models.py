# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField
from common.utils.unique_slug import unique_slugify


# Models
class Badge(CMSPlugin):
    """Badge."""

    class Meta:
        verbose_name = _('Badge')
        verbose_name_plural = _('Badge')

    title = models.CharField(
        _('Title H1'),
        max_length=255,
    )
    subtitle = models.CharField(
        _('Title H1'),
        max_length=255,
        blank=True,
        null=True,
    )
