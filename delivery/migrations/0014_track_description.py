# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0013_auto_20170622_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
