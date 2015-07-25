# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0005_auto_20150721_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
