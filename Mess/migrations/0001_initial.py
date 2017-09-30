# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('item', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
    ]