# Generated by Django 2.2.17 on 2023-11-10 22:26

import datetime
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoBox',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='infobox_infobox', serialize=False, to='cms.CMSPlugin')),
                ('is_visible', models.BooleanField(default=True, verbose_name='is visible')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('text', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('start_date', models.DateField(default=datetime.date.today, verbose_name='Start date')),
                ('end_date', models.DateField(default=datetime.date.today, verbose_name='End date')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
