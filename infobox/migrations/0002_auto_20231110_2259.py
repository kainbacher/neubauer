# Generated by Django 2.2.17 on 2023-11-10 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infobox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infobox',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='infobox',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start date'),
        ),
    ]
