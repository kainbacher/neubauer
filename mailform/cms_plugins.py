from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import ContactForm
from .forms import Formular


class ContactFormPlugin(CMSPluginBase):
    """Contact form plugin."""
    model = ContactForm
    name = _('Contact form')
    render_template = "mailform.html"
    cache = False

    def render(self, context, instance, placeholder):
        request = context['request']

        if request.method == "POST":
            form = Formular(request.POST)
            if form.is_valid():
                form.send_notification_to_sender(
                    instance.receiver_email)
                form.send_notification_to_user(
                    instance,
                    instance.receiver_email
                )
                form = Formular()
                context.update({
                    'mailform_sent': True,
                    'form': form,
                    'instance': instance,
                })
            else:
                context.update({
                    'form_invalid': True,
                    'form': form,
                    'instance': instance,
                })
            return context
        else:
            form = Formular()
            context.update({
                'instance': instance,
                'form': form,
            })
            return context


plugin_pool.register_plugin(ContactFormPlugin)
