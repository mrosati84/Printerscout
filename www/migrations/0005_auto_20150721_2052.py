# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0004_auto_20150721_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='referer',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Referente', blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='first_visit_black',
            field=models.IntegerField(null=True, verbose_name=b'Contatore nero', blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='first_visit_color',
            field=models.IntegerField(null=True, verbose_name=b'Contatore colore', blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='second_visit_black',
            field=models.IntegerField(null=True, verbose_name=b'Contatore nero', blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='second_visit_color',
            field=models.IntegerField(null=True, verbose_name=b'Contatore colore', blank=True),
        ),
    ]
