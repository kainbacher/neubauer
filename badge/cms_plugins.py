# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from badge.models import Badge


@plugin_pool.register_plugin
class BadgePlugin(CMSPluginBase):
    """BadgePlugin."""

    model = Badge
    name = _('Badge')
    render_template = "badge.html"
