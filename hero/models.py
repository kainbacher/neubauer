# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField


# Models
class Hero(CMSPlugin):
    """Hero."""

    class Meta:
        verbose_name = _('Hero')
        verbose_name_plural = _('Hero')

    title = models.CharField(
        _('Title H1'),
        max_length=255,
        blank=True,
        null=True,
    )
    subtitle = models.CharField(
        _('Subtitle H2'),
        max_length=255,
        blank=True,
        null=True
    )
    image = FilerImageField(
        verbose_name=_('Image'),
        related_name="hero_image",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    IMAGE_HIGHT_CHOICES = (
        ('vh-100', _('Height 100%')),
        ('vh-75', _('Height 75%')),
        ('vh-50', _('Height 50%')),
    )
    image_height = models.CharField(
        _("Image height"),
        choices=IMAGE_HIGHT_CHOICES,
        default=IMAGE_HIGHT_CHOICES[0][0],
        max_length=50
    )

    content = PlaceholderField(
        'content_hero'
    )
    TEMPLATE_CHOICES = (
        ('content-bottom', _('Content bottom')),
        ('content-top', _('Content top')),
    )
    template = models.CharField(
        _("Template"),
        choices=TEMPLATE_CHOICES,
        default=TEMPLATE_CHOICES[0][0],
        max_length=50
    )
