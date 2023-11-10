# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField


# Models
class InfoBox(CMSPlugin):
    """InfoBox."""

    is_visible = models.BooleanField(
        _("is visible"),
        default=True,
        help_text=_("Show InfoBox on page. If start date and end date are set, Info Box is only shown between start_date and end_date."),
    )
    title = models.CharField(
        _("Title"),
        max_length=255
    )
    text = HTMLField(
        verbose_name=_("Text"),
        configuration="CKEDITOR_SETTINGS_MODEL",
        blank=True,
    )
    start_date = models.DateField(
        _("Start date"),
        blank=True,
        null=True,
    )
    end_date = models.DateField(
        _("End date"),
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.title}"

    def show(self):
        """
        Show InfoBox if start_date and end_date are set and
        today is between start_date and end_date.
        """
        if self.start_date is None and self.end_date is None:
            return self.is_visible
        return self.is_visible and self.start_date <= datetime.date.today() <= self.end_date
