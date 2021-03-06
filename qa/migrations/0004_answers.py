# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-03 07:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20180802_0226'),
        ('qa', '0003_auto_20180803_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.CharField(max_length=200)),
                ('pubtime', models.DateTimeField(default=datetime.datetime.now)),
                ('post_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feeds.Registers')),
                ('ques_text', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.Questions')),
            ],
        ),
    ]
