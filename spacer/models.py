# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin


# Models
class Spacer(CMSPlugin):
    """Spacer."""

    class Meta:
        verbose_name = _('Spacer')
        verbose_name_plural = _('Spacer')

    DISTANCE_CHOICES = (
        ('1', _('1')),
        ('2', _('2')),
        ('3', _('3')),
        ('4', _('4')),
        ('5', _('5')),
        ('6', _('6')),
        ('7', _('7')),
        ('8', _('8')),
        ('9', _('9')),
        ('10', _('10')),
    )

    distance = models.CharField(
        _("Distance"),
        choices=DISTANCE_CHOICES,
        default=DISTANCE_CHOICES[0][0],
        max_length=10
    )
