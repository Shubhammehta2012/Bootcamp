# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-03 00:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20180802_0226'),
        ('qa', '0002_auto_20180802_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feeds.Registers'),
        ),
        migrations.AddField(
            model_name='questions',
            name='pub_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]