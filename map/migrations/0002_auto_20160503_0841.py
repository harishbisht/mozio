# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='Coordinates',
        ),
        migrations.AddField(
            model_name='map',
            name='Lat',
            field=models.FloatField(null=True, verbose_name='Latitude', blank=True),
        ),
        migrations.AddField(
            model_name='map',
            name='Lon',
            field=models.FloatField(null=True, verbose_name='Longitude', blank=True),
        ),
    ]
