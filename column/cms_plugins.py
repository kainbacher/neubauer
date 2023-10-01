from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import MultiColumns, Column


class MultiColumnPlugin(CMSPluginBase):
    model = MultiColumns
    module = _("Multi Columns")
    name = _("Multi Columns")
    render_template = "cms/plugins/multi_column.html"
    allow_children = True
    child_classes = ["ColumnPlugin"]


class ColumnPlugin(CMSPluginBase):
    model = Column
    module = _("Multi Columns")
    name = _("Column")
    render_template = "cms/plugins/column.html"
    parent_classes = ["MultiColumnPlugin"]
    allow_children = True


plugin_pool.register_plugin(MultiColumnPlugin)
plugin_pool.register_plugin(ColumnPlugin)
