# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    """PersonAdmin."""

    list_display = [
        'name',
        'function',
        'position',
        'is_visible',
    ]
    list_filter = [
        'is_visible',
    ]
    list_editable = [
        'position'
    ]
    ordering = [
        'position'
    ]
    search_fields = [
        'name',
        'function'
    ]


admin.site.register(Person, PersonAdmin)
