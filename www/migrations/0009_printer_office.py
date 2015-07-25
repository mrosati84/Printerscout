# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0008_auto_20150725_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='office',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Ufficio', blank=True),
        ),
    ]
