# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-18 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaming_patrada', '0013_auto_20170218_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]