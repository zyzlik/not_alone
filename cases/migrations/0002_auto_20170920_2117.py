# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-20 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import fields


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='step_number',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='case',
            name='title',
            field=fields.MaxCharField(help_text='Не более 255 символов<br/>Не более 255 символов<br/>Не более 255 символов', max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='body',
            field=fields.MaxCharField(help_text='Не более 255 символов<br/>Не более 255 символов<br/>Не более 255 символов', max_length=255, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='title',
            field=fields.MaxCharField(help_text='Не более 255 символов<br/>Не более 255 символов<br/>Не более 255 символов', max_length=255, verbose_name='Title'),
        ),
    ]
