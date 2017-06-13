# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 20:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postman_order', to='delivery.Order'),
        ),
    ]
