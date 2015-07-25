# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0010_auto_20150725_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='ip_address',
            field=models.CharField(max_length=16, null=True, verbose_name=b'Indirizzo IP', blank=True),
        ),
    ]
