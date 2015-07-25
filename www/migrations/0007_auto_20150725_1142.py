# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0006_printer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='label',
            field=models.IntegerField(null=True, verbose_name=b'Etichetta', blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='image',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'Immagine', blank=True),
        ),
    ]
