# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 21:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_lake_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lake',
            old_name='url',
            new_name='link',
        ),
    ]