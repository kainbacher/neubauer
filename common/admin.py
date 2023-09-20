# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


# Sitewide Admin Action
def duplicate_entry(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate_entry.short_description = _("Duplicate selected record")

# Export Actions
admin.site.add_action(duplicate_entry, 'duplicate_entry')
