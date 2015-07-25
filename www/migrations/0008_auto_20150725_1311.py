# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0007_auto_20150725_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, null=True, verbose_name=b'Marca stampante', blank=True)),
            ],
            options={
                'verbose_name': 'Marca stampante',
                'verbose_name_plural': 'Marche stampanti',
            },
        ),
        migrations.AddField(
            model_name='printer',
            name='brand',
            field=models.ForeignKey(verbose_name=b'Marca', blank=True, to='www.Brand', null=True),
        ),
    ]
