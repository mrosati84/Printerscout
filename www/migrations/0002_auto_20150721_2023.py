# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Azienza', 'verbose_name_plural': 'Aziende'},
        ),
        migrations.AlterModelOptions(
            name='printer',
            options={'verbose_name': 'Stampante', 'verbose_name_plural': 'Stampanti'},
        ),
        migrations.AddField(
            model_name='printer',
            name='model',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Modello'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Azienda'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='area',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Area'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='company',
            field=models.ForeignKey(verbose_name=b'Azienda', to='www.Company'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='floor',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Piano'),
        ),
    ]
