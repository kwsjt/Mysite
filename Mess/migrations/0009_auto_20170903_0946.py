# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 04:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mess', '0008_userprofile_mess'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extras',
            old_name='amount',
            new_name='extra',
        ),
    ]