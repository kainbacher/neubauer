# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import Person, TeamList


@plugin_pool.register_plugin
class TeamListPlugin(CMSPluginBase):
    """TeamListPlugin."""

    model = TeamList
    name = _('Team List')
    text_enabled = True
    render_template = "team_list.html"

    def render(self, context, instance, placeholder):

        if instance.team == 'doctor':
            object_list = Person.objects.get_doctors()
        elif instance.team == 'team':
            object_list = Person.objects.get_team()
        else:
            object_list = Person.objects.get_all()

        context.update({
            'instance': instance,
            'object_list': object_list,
            'placeholder': placeholder,
        })
        return context
