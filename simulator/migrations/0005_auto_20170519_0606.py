# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0004_auto_20170518_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildinggroup',
            name='acceleration',
            field=models.FloatField(default=0.8),
        ),
        migrations.AddField(
            model_name='buildinggroup',
            name='carCapacity',
            field=models.IntegerField(default=13),
        ),
        migrations.AddField(
            model_name='buildinggroup',
            name='doorClosingTime',
            field=models.FloatField(default=3),
        ),
        migrations.AddField(
            model_name='buildinggroup',
            name='doorOpeningTime',
            field=models.FloatField(default=2),
        ),
        migrations.AddField(
            model_name='buildinggroup',
            name='jerk',
            field=models.FloatField(default=1.2),
        ),
        migrations.AddField(
            model_name='buildinggroup',
            name='passengerTransferTime',
            field=models.FloatField(default=0.9),
        ),
        migrations.AddField(
            model_name='buildinggroup',
            name='speed',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='buildinggroup',
            name='carsNumber',
            field=models.IntegerField(default=2),
        ),
    ]
