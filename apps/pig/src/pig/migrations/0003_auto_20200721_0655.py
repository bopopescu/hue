# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-21 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pig', '0002_auto_20200714_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pigscript',
            name='data',
            field=models.TextField(default=b'{"name": "", "parameters": [], "script": "", "hadoopProperties": [], "properties": [], "resources": [], "job_id": null}'),
        ),
    ]
