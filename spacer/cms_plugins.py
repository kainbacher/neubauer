from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import Spacer


class SpacerPlugin(CMSPluginBase):
    """SpacerPlugin."""
    model = Spacer
    name = _('Spacer')
    render_template = "spacer.html"


plugin_pool.register_plugin(SpacerPlugin)
