# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-06 22:09
from __future__ import unicode_literals

from django.db import migrations
import fields


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0007_auto_20171006_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstage',
            name='stage',
        ),
        migrations.RemoveField(
            model_name='userstage',
            name='user',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='users',
        ),
        migrations.AlterField(
            model_name='case',
            name='title',
            field=fields.MaxCharField(help_text='Не более 255 символов<br/>Не более 255 символов<br/>Не более 255 символов', max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='title',
            field=fields.MaxCharField(help_text='Не более 255 символов<br/>Не более 255 символов<br/>Не более 255 символов', max_length=255, verbose_name='Title'),
        ),
        migrations.DeleteModel(
            name='UserStage',
        ),
    ]
