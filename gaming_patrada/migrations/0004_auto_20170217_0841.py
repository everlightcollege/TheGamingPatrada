# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-17 05:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gaming_patrada', '0003_auto_20170217_0825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='games',
            options={'verbose_name_plural': 'Games'},
        ),
    ]