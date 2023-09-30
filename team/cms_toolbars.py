from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar


@toolbar_pool.register
class TeamToolbar(CMSToolbar):
    def populate(self):
        menu = self.toolbar.get_or_create_menu('modules', _('Modules'))

        url = reverse('admin:team_person_changelist')
        menu.add_sideframe_item(_('Team'), url=url)

        menu.add_break()
