# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0023_auto_20170606_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='simulator.BuildingTypes'),
        ),
    ]
