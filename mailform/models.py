from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField


class ContactForm(CMSPlugin):
    """Contact Form."""
    class Meta:
        verbose_name = _('Contact form')
        verbose_name_plural = _('Contact forms')

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        blank=True,
        null=True,
    )
    text = HTMLField(
        verbose_name=_('Text'),
        blank=True,
        help_text=_('This text is shown above the form.')
    )
    image = FilerImageField(
        verbose_name=_('Image'),
        related_name="contact_form_image",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    facebook_evaluation_link = models.URLField(
        verbose_name=_('Facebook evaluation link'),
        blank=True,
        null=True,
    )
    google_evaluation_link = models.URLField(
        verbose_name=_('Google evaluation link'),
        blank=True,
        null=True,
    )
    receiver_email = models.EmailField(
        verbose_name=_('receiver email')
    )
    sent_message = HTMLField(
        verbose_name=_('Text after sending the form'),
        blank=True,
        help_text=_('This message is shown in the info box when the user has sent the form.')
    )
    email_subject = models.CharField(
        _('Email Subject'),
        max_length=255,
        blank=True,
        null=True,
    )
    email_text = HTMLField(
        verbose_name=_('Text in the email'),
        blank=True,
        help_text=_('This message is shown in the email the user gets.')
    )
