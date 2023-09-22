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
class Contact(CMSPlugin):
    """Contact."""

    class Meta:
        verbose_name = _('Contact Block')
        verbose_name_plural = _('Contact Blocks')

    title = models.CharField(
        _('Title H1'),
        max_length=255,
        blank=True,
        null=True,
    )
    image = FilerImageField(
        verbose_name=_('Image'),
        related_name="contact_image",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
