from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import AppointmentForm
from .forms import Formular


class AppointmentFormPlugin(CMSPluginBase):
    """Appointment form plugin."""
    model = AppointmentForm
    name = _('Appointment form')
    render_template = "formappointment/appointmentform.html"
    cache = False

    def render(self, context, instance, placeholder):
        request = context['request']

        if request.method == "POST":
            app_form = Formular(request.POST)
            if app_form.is_valid():
                app_form.send_notification_to_sender(
                    instance.receiver_email)
                app_form.send_notification_to_user(
                    instance,
                    instance.receiver_email
                )
                app_form = Formular()
                context.update({
                    'appointment_form_sent': True,
                    'app_form': app_form,
                    'instance': instance,
                })
            else:
                context.update({
                    'form_invalid': True,
                    'app_form': app_form,
                    'instance': instance,
                })
            return context
        else:
            app_form = Formular()
            context.update({
                'instance': instance,
                'app_form': app_form,
            })
            return context


plugin_pool.register_plugin(AppointmentFormPlugin)
