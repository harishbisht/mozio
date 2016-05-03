# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20160503_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Lat', models.FloatField(null=True, verbose_name='Latitude', blank=True)),
                ('Lon', models.FloatField(null=True, verbose_name='Longitude', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='map',
            name='Lat',
        ),
        migrations.RemoveField(
            model_name='map',
            name='Lon',
        ),
        migrations.AddField(
            model_name='location',
            name='Dealer',
            field=models.ForeignKey(related_name='MapLocation', to='map.Map'),
        ),
    ]
