# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 22:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160323_2149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lake',
            old_name='link',
            new_name='url',
        ),
    ]
