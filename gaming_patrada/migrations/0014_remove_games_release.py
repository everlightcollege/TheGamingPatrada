# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 16:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gaming_patrada', '0013_auto_20170312_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='release',
        ),
    ]
