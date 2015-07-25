# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_auto_20150721_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Azienda', blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='area',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Area', blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='company',
            field=models.ForeignKey(verbose_name=b'Azienda', blank=True, to='www.Company', null=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='floor',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Piano', blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='model',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Modello', blank=True),
        ),
    ]
