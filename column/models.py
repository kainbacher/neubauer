from cms.models import CMSPlugin
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField


WIDTH_CHOICES = (
    ("0", _("auto cols")),
    ("1", _("8%, 1 col")),
    ("2", _("16%, 2 cols")),
    ("3", _("25%, 3 cols")),
    ("4", _("33,3%, 4 col")),
    ("5", _("42%, 5 cols")),
    ("6", _("50%, 6 cols")),
    ("7", _("58%, 7 cols")),
    ("8", _("66%, 8 cols")),
    ("9", _("75%, 9 cols")),
    ("10", _("84%, 10 cols")),
    ("11", _("92%, 11 cols")),
    ("12", _("100%, 12 cols")),
)

COLOR_CHOICES = (
    ("white", _("white")),
    ("cyan", _("cyan")),
)

MARGIN_CHOICES = (
    ("0", _("0")),
    ("1", _("1")),
    ("2", _("2")),
    ("3", _("3")),
    ("4", _("4")),
    ("5", _("5")),
)

PADDING_CHOICES = (
    ("0", _("0")),
    ("1", _("1")),
    ("2", _("2")),
    ("3", _("3")),
    ("4", _("4")),
    ("5", _("5")),
    ("6", _("6")),
    ("7", _("7")),
    ("8", _("8")),
    ("9", _("9")),
    ("10", _("10")),
)

OFFSET_CHOICES = (
    ("-", _("not set")),
    ("0", _("0")),
    ("1", _("1")),
    ("2", _("2")),
    ("3", _("3")),
    ("4", _("4")),
    ("5", _("5")),
    ("6", _("6")),
    ("7", _("7")),
    ("8", _("8")),
    ("9", _("9")),
    ("10", _("10")),
    ("11", _("11")),
)

ORDER_CHOICES = (
    ("0", _("0")),
    ("1", _("1")),
    ("2", _("2")),
    ("3", _("3")),
    ("4", _("4")),
    ("5", _("5")),
    ("6", _("6")),
    ("7", _("7")),
    ("8", _("8")),
    ("9", _("9")),
    ("10", _("10")),
)


class MultiColumns(CMSPlugin):
    """
    A plugin that has sub Column classes
    """

    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name="%(app_label)s_%(class)s",
        parent_link=True,
        on_delete=models.CASCADE,
    )
    background_color = models.CharField(
        _("background color"),
        choices=COLOR_CHOICES,
        default=COLOR_CHOICES[0][0],
        max_length=50,
    )
    padding = models.CharField(
        _("padding"),
        choices=PADDING_CHOICES,
        default=PADDING_CHOICES[0][0],
        max_length=50,
    )
    is_fluid = models.BooleanField(_("fluid"), default=False)
    has_gutters = models.BooleanField(_("gutters"), default=True)
    anchor_id = models.SlugField(
        _("Anchor Id"),
        blank=True,
        null=True,
        help_text=_("unique id to create a anchor to this point"),
    )

    def __str__(self):
        plugins = self.child_plugin_instances or []
        return _("%s columns") % len(plugins)


class Column(CMSPlugin):
    """
    A Column for the MultiColumns Plugin
    """

    is_vertical_centered = models.BooleanField(
        _("vertical centered"),
        default=False
    )
    show_box = models.BooleanField(
        _("show box"),
        default=False
    )
    width_md = models.CharField(
        _("width md"),
        choices=WIDTH_CHOICES,
        default=WIDTH_CHOICES[6][0],
        max_length=50
    )
    offset_md = models.CharField(
        _("offset md"),
        choices=OFFSET_CHOICES,
        default=OFFSET_CHOICES[0][0],
        max_length=50,
    )
    width_lg = models.CharField(
        _("width lg"),
        choices=WIDTH_CHOICES,
        default=WIDTH_CHOICES[0][0],
        max_length=50
    )
    offset_lg = models.CharField(
        _("offset lg"),
        choices=OFFSET_CHOICES,
        default=OFFSET_CHOICES[0][0],
        max_length=50,
    )
    width_xl = models.CharField(
        _("width xl"),
        choices=WIDTH_CHOICES,
        default=WIDTH_CHOICES[0][0],
        max_length=50
    )
    offset_xl = models.CharField(
        _("offset xl"),
        choices=OFFSET_CHOICES,
        default=OFFSET_CHOICES[0][0],
        max_length=50,
    )
    width_xxl = models.CharField(
        _("width xxl"),
        choices=WIDTH_CHOICES,
        default=WIDTH_CHOICES[0][0],
        max_length=50,
    )
    offset_xxl = models.CharField(
        _("offset xxl"),
        choices=OFFSET_CHOICES,
        default=OFFSET_CHOICES[0][0],
        max_length=50,
    )
    # Ordering
    order = models.CharField(
        _("order"),
        choices=ORDER_CHOICES,
        default=ORDER_CHOICES[0][0],
        max_length=50
    )
    order_md = models.CharField(
        _("order md"),
        choices=ORDER_CHOICES,
        default=ORDER_CHOICES[0][0],
        max_length=50
    )
    order_lg = models.CharField(
        _("order lg"),
        choices=ORDER_CHOICES,
        default=ORDER_CHOICES[0][0],
        max_length=50
    )
    order_xl = models.CharField(
        _("order xl"),
        choices=ORDER_CHOICES,
        default=ORDER_CHOICES[0][0],
        max_length=50
    )
    order_xxl = models.CharField(
        _("order xxl"),
        choices=ORDER_CHOICES,
        default=ORDER_CHOICES[0][0],
        max_length=50,
    )
    margin_top = models.CharField(
        _("margin top"),
        choices=MARGIN_CHOICES,
        default=MARGIN_CHOICES[0][0],
        max_length=50,
    )
    margin_bottom = models.CharField(
        _("margin bottom"),
        choices=MARGIN_CHOICES,
        default=MARGIN_CHOICES[0][0],
        max_length=50,
    )
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name="%(app_label)s_%(class)s",
        parent_link=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "md:%s lg:%s xl:%s" % (self.width_md, self.width_lg, self.width_xl)
