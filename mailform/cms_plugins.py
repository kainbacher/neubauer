import os
from django import dispatch
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.forms.fields import CharField
from django import forms
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, select_template
from django.http import HttpResponseRedirect

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from mailform.models import ContactForm
from mailform.forms import Formular


class ContactFormPlugin(CMSPluginBase):
    model = ContactForm
    name = _('Contact form')
    render_template = "mailform.html"
    cache = False

    def render(self, context, instance, placeholder):
        request = context['request']

        if request.method == "POST":
            form = Formular(request.POST)
            if form.is_valid():
                form.send_notification_to_sender(
                    instance.receiver_email)
                form.send_notification_to_user(
                    instance,
                    instance.receiver_email
                )
                context.update({
                    'form_sent': True,
                    'instance': instance,
                })
            else:
                context.update({
                    'form_invalid': True,
                    'form': form,
                    'instance': instance,
                })
            return context
        else:
            form = Formular()
            context.update({
                'instance': instance,
                'form': form,
            })
            return context


plugin_pool.register_plugin(ContactFormPlugin)
