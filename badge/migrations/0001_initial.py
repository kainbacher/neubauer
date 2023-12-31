# Generated by Django 2.2.17 on 2023-09-21 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='badge_badge', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, verbose_name='Title H1')),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title H1')),
            ],
            options={
                'verbose_name': 'Badge',
                'verbose_name_plural': 'Badge',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
