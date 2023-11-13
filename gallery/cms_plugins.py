# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import Gallery, Image


class ImageInline(admin.StackedInline):
    """Image Inline."""
    model = Image
    extra = 0
    ordering = ["position"]
    fk_name = "gallery"


@plugin_pool.register_plugin
class GalleryPlugin(CMSPluginBase):
    """GalleryPlugin."""

    class Media:
        """Media."""
        js = ["js/widget_ordering.js"]

    model = Gallery
    name = _("Gallery")
    render_template = "gallery.html"
    inlines = [
        ImageInline,
    ]

    def render(self, context, instance, placeholder):

        if instance.sorting == "numbers":
            gallery = instance.gallery.all().order_by("position")
        else:
            gallery = instance.gallery.all().order_by("?")

        context.update(
            {
                "instance": instance,
                "gallery": gallery,
                "placeholder": placeholder,
            }
        )
        return context
