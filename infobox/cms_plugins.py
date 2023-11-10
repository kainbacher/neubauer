# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import InfoBox


@plugin_pool.register_plugin
class InfoBoxPlugin(CMSPluginBase):
    """InfoBoxPlugin."""

    model = InfoBox
    name = _("Information Box")
    render_template = "infobox.html"

    # def render(self, context, instance, placeholder):
    #     object_list = News.objects.get_latest(instance.max_articles)

    #     context.update(
    #         {
    #             "instance": instance,
    #             "object_list": object_list,
    #             "placeholder": placeholder,
    #         }
    #     )
    #     return context
