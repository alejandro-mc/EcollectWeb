# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-05 01:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newentry', '0005_remove_sensors_sensorid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensordata',
            old_name='preassure',
            new_name='pressure',
        ),
        migrations.RenameField(
            model_name='weatherdata',
            old_name='preassure',
            new_name='pressure',
        ),
    ]
