# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page


# Models
class Badge(CMSPlugin):
    """Badge."""

    class Meta:
        verbose_name = _('Badge')
        verbose_name_plural = _('Badge')

    is_visible = models.BooleanField(
        _('Is visible'),
        default=True,
    )
    title = models.CharField(
        _('Title H1'),
        max_length=255,
    )
    subtitle = models.CharField(
        _('Title H1'),
        max_length=255,
        blank=True,
        null=True,
    )
    internal_link = models.ForeignKey(
        Page,
        verbose_name=_('Internal link'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def get_link(self):
        link = ''

        if self.internal_link:
            ref_page = self.internal_link
            link = ref_page.get_absolute_url()

            # simulate the call to the unauthorized CMSPlugin.page property
            cms_page = self.placeholder.page if self.placeholder_id else None

            # first, we check if the placeholder the plugin is attached to
            # has a page. Thus the check "is not None":
            if cms_page is not None:
                if getattr(cms_page, 'node', None):
                    cms_page_site_id = getattr(cms_page.node, 'site_id', None)
                else:
                    cms_page_site_id = getattr(cms_page, 'site_id', None)
            # a plugin might not be attached to a page and thus has no site
            # associated with it. This also applies to plugins inside
            # static placeholders
            else:
                cms_page_site_id = None

            # now we do the same for the reference page the plugin links to
            # in order to compare them later
            if cms_page is not None:
                if getattr(cms_page, 'node', None):
                    ref_page_site_id = ref_page.node.site_id
                else:
                    ref_page_site_id = ref_page.site_id
            # if no external reference is found the plugin links to the
            # current page
            else:
                ref_page_site_id = Site.objects.get_current().pk

            if ref_page_site_id != cms_page_site_id:
                ref_site = Site.objects._get_site_by_id(
                    ref_page_site_id).domain
                link = f'//{ref_site}{link}'

        return link
