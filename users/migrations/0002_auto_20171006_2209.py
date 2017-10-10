# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-06 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0008_auto_20171006_2209'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cases',
        ),
        migrations.AddField(
            model_name='user',
            name='stages',
            field=models.ManyToManyField(to='cases.Case', verbose_name='Stages'),
        ),
    ]