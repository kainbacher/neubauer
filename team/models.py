# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField


TEAM_CHOICES = (
    ('doctor', _('Doctor')),
    ('team', _('Team ')),
)


# Managers
class PersonManager(models.Manager):
    """PersonManager."""

    def get_all(self):
        """Get all visible persons."""
        return super(PersonManager, self) \
            .filter(is_visible=True).order_by('position')

    def get_doctors(self):
        """Get all visible doctors."""
        return super(PersonManager, self) \
            .filter(is_visible=True, team='doctor').order_by('position')

    def get_team(self):
        """Get all visible team."""
        return super(PersonManager, self) \
            .filter(is_visible=True, team='team').order_by('position')


# Models
class Person(models.Model):
    """Person."""

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Person')

    is_visible = models.BooleanField(
        _('is_visible'),
        default=True
    )
    name = models.CharField(
        _('Name'),
        max_length=255,
        help_text=_('Full name')
    )
    function = models.CharField(
        _('Function'),
        blank=True,
        max_length=255
    )
    image = FilerImageField(
        verbose_name=_('Image'),
        related_name="person_image",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    team = models.CharField(
        _("Team"),
        choices=TEAM_CHOICES,
        default=TEAM_CHOICES[0][0],
        max_length=50
    )
    position = models.PositiveIntegerField(
        _('Position'),
        blank=True,
        null=True
    )
    objects = PersonManager()

    def __str__(self):
        return f'{self.name}'


class TeamList(CMSPlugin):
    """TeamPlugin."""

    title = models.CharField(
        _('Title'),
        max_length=255,
        blank=True,
        null=True,
    )
    team = models.CharField(
        _("Team"),
        choices=TEAM_CHOICES,
        default=TEAM_CHOICES[0][0],
        max_length=50
    )
