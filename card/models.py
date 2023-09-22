# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from common.utils.unique_slug import unique_slugify


# Models
class Card(CMSPlugin):
    """Card."""

    class Meta:
        verbose_name = _('Card')
        verbose_name_plural = _('Cards')

    title = models.CharField(
        _('Title H1'),
        max_length=255,
        blank=True,
        null=True,
    )
    text = HTMLField(
        configuration='CKEDITOR_SETTINGS_MODEL',
        blank=True,
    )
    image = FilerImageField(
        verbose_name=_('Image'),
        related_name="card_image",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
