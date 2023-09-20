from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar


@toolbar_pool.register
class NewsToolbar(CMSToolbar):
    def populate(self):
        menu = self.toolbar.get_or_create_menu('modules', _('Modules'))

        url = reverse('admin:filer_folder_changelist')
        menu.add_sideframe_item(_('Mediapool'), url=url)

        menu.add_break()
