# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Coordinates', models.DecimalField(max_digits=9, decimal_places=6)),
                ('Dealername', models.ManyToManyField(to='provider.Provider', blank=True)),
            ],
        ),
    ]
