# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 20:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160827_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='when',
        ),
    ]
