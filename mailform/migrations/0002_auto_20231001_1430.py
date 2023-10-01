# Generated by Django 2.2.17 on 2023-10-01 14:30

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mailform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='facebook_evaluation_link',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook evaluation link'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='google_evaluation_link',
            field=models.URLField(blank=True, null=True, verbose_name='Google evaluation link'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='text',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, help_text='This text is shown above the form.', verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='email_text',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, help_text='This message is shown in the email the user gets.', verbose_name='Text in the email'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='sent_message',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, help_text='This message is shown in the info box when the user has sent the form.', verbose_name='Text after sending the form'),
        ),
    ]
