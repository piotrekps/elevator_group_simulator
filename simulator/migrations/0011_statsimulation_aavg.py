# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0010_auto_20170522_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='statsimulation',
            name='aavg',
            field=models.FloatField(default=2),
        ),
    ]