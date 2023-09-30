from django import forms
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from captcha.fields import ReCaptchaField


class Formular(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    location = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    content = forms.CharField(required=False, widget=forms.Textarea())
    quick_appointment = forms.BooleanField(required=False)
    already_customer = forms.BooleanField(required=False)
    information_channel = forms.CharField(required=True)
    data_protection = forms.BooleanField(required=True)

    # check1 = forms.CharField(widget=forms.HiddenInput())

    def send_notification_to_sender(self, receiver_email):
        email_message = EmailMessage(
            _('Request from website'),
            render_to_string("sender_email.txt", {
                'data': self.cleaned_data,
            }),
            settings.EMAIL_HOST_USER,  # from
            [receiver_email],  # to
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
            settings.EMAIL_HOST_USER,  # from
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
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['location'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control h-100 grow-1'

        self.fields['quick_appointment'].widget.attrs['class'] = 'form-check-input'
        self.fields['already_customer'].widget.attrs['class'] = 'form-check-input'
        self.fields['data_protection'].widget.attrs['class'] = 'form-check-input'
