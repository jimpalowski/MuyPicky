# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-31 21:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restraunts', '0002_restraunt_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restraunt',
            new_name='RestrauntLocation',
        ),
    ]
