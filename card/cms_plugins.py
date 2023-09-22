# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from card.models import Card


@plugin_pool.register_plugin
class CardPlugin(CMSPluginBase):
    """CardPlugin."""

    model = Card
    name = _('Card')
    render_template = "card.html"
