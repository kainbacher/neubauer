# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from contact.models import Contact


@plugin_pool.register_plugin
class ContactPlugin(CMSPluginBase):
    """ContactPlugin."""

    model = Contact
    name = _('Contact Block')
    render_template = "contact.html"
