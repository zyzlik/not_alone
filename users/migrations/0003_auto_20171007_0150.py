# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-07 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171006_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='stages',
            field=models.ManyToManyField(to='cases.Stage', verbose_name='Stages'),
        ),
    ]
