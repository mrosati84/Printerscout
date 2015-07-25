# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0003_auto_20150721_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='first_visit',
            field=models.DateField(null=True, verbose_name=b'Data prima visita', blank=True),
        ),
        migrations.AddField(
            model_name='printer',
            name='first_visit_black',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='printer',
            name='first_visit_color',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='printer',
            name='second_visit',
            field=models.DateField(null=True, verbose_name=b'Data seconda visita', blank=True),
        ),
        migrations.AddField(
            model_name='printer',
            name='second_visit_black',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='printer',
            name='second_visit_color',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
