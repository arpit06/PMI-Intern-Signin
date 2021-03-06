# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-24 16:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clockin', '0021_auto_20170530_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='summary',
            field=models.CharField(default='N/A', max_length=5000, verbose_name='Summary'),
        ),
        migrations.AlterField(
            model_name='work',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='work',
            name='time_in',
            field=models.TimeField(blank=True, default=datetime.time(12, 47, 1, 371786), verbose_name='Time In'),
        ),
        migrations.AlterField(
            model_name='work',
            name='time_out',
            field=models.TimeField(blank=True, default=datetime.time(12, 47, 1, 371831), verbose_name='Time Out'),
        ),
    ]
