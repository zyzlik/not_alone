# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-20 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import fields


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0003_auto_20170920_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='title',
            field=fields.MaxCharField(help_text='Не более 255 символов<br/>Не более 255 символов<br/>Не более 255 символов', max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='stage',
            name='title',
            field=fields.MaxCharField(help_text='Не более 255 символов<br/>Не более 255 символов<br/>Не более 255 символов', max_length=255, verbose_name='Title'),
        ),
    ]
