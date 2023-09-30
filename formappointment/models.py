from django.db import models
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField
from cms.models import CMSPlugin


class AppointmentForm(CMSPlugin):
    class Meta:
        verbose_name = _('Appointment form')
        verbose_name_plural = _('Appointment forms')

    receiver_email = models.EmailField(
        verbose_name=_('receiver email')
    )
    sent_message = HTMLField(
        verbose_name=_('send mesage'),
        blank=True,
        help_text=_('this message is shown when the user has sent the form')
    )
    email_subject = models.CharField(
        _('Email Subject'),
        max_length=255,
        blank=True,
        null=True,
    )
    email_text = HTMLField(
        verbose_name=_('email_text'),
        blank=True,
        help_text=_('this message is shown in the email the user gets')
    )
