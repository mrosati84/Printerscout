# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0009_printer_office'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=140, null=True, verbose_name=b'Marca stampante', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=140, null=True, verbose_name=b'Azienda', blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='area',
            field=models.CharField(max_length=150, null=True, verbose_name=b'Area', blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='floor',
            field=models.CharField(max_length=120, null=True, verbose_name=b'Piano', blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='model',
            field=models.CharField(max_length=150, null=True, verbose_name=b'Modello', blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='office',
            field=models.CharField(max_length=120, null=True, verbose_name=b'Ufficio', blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='referer',
            field=models.CharField(max_length=150, null=True, verbose_name=b'Referente', blank=True),
        ),
    ]
