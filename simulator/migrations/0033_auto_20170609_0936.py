# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0032_auto_20170609_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulator.StandardUsers'),
        ),
    ]
