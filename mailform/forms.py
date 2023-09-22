from django import forms
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from captcha.fields import ReCaptchaField


class Formular(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    content = forms.CharField(required=False, widget=forms.Textarea())
    # check1 = forms.CharField(widget=forms.HiddenInput())

    def send_notification_to_sender(self, receiver_email):
        email_message = EmailMessage(
            _('Request from website'),
            render_to_string("sender_email.txt", {
                'data': self.cleaned_data,
            }),
            settings.EMAIL_HOST_USER, # from
            [receiver_email], # to
            bcc=['roland@kainbacher.io'],
            headers={
                'Reply-To': self.cleaned_data['email']
            }
        )
        email_message.send(fail_silently=True)

    def send_notification_to_user(self, instance, email_from):
        email_to = self.cleaned_data['email']
        email_text = instance.email_text

        html_content = render_to_string("notification_email.html", {
            'data': self.cleaned_data,
            'email_text': email_text,
        })

        email_message = EmailMultiAlternatives(
            instance.email_subject,
            "HTML",
            settings.EMAIL_HOST_USER, # from
            [email_to],  # to
            bcc=['roland@kainbacher.io'],
            headers={
                'Reply-To': email_from
            }
        )

        email_message.attach_alternative(html_content, "text/html")
        email_message.send(fail_silently=True)

    def __init__(self, *args, **kwargs):
        super(Formular, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'
