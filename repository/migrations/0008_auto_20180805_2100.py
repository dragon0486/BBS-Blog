# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-05 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0007_auto_20180803_1946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trouble',
            old_name='processor',
            new_name='processer',
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]