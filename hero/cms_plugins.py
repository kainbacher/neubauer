# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from hero.models import Hero


@plugin_pool.register_plugin
class HeroPlugin(CMSPluginBase):
    """HeroPlugin."""

    model = Hero
    name = _('Hero')
    render_template = "hero.html"
