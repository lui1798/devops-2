# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-26 08:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20180326_1610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterModelOptions(
            name='usergroup',
            options={'verbose_name': '用户组', 'verbose_name_plural': '用户组'},
        ),
    ]
