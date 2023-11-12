from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField


# !models
# ----------------------------------------------------------------------
class Gallery(CMSPlugin):
    """Gallery."""

    VIEW_CHOICES = (
        ('grid', _('Grid Layout')),
        # ('slider', _('Slider')),
    )
    view = models.CharField(
        _("Gallery View"),
        choices=VIEW_CHOICES,
        default=VIEW_CHOICES[0][0],
        max_length=50
    )

    def copy_relations(self, oldinstance):
        try:
            self.gallery.all().delete()
        except Exception:
            pass

        for image in oldinstance.gallery.all():
            image.pk = None
            image.gallery = self
            image.save()


class Image(models.Model):
    """Image."""

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    image = FilerImageField(
        related_name="gallery_image",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    position = models.PositiveIntegerField(
        _('Position'),
        blank=True,
        null=True
    )
    gallery = models.ForeignKey(
        Gallery,
        related_name="gallery",
        on_delete=models.CASCADE,
    )