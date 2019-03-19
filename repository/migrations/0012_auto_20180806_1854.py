# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-06 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0011_auto_20180806_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32)),
                ('code', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': '操作表',
            },
        ),
        migrations.CreateModel(
            name='Permission2Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Action')),
            ],
            options={
                'verbose_name_plural': '权限表',
            },
        ),
        migrations.RenameModel(
            old_name='Permission2Role',
            new_name='Permission2Action2Role',
        ),
        migrations.AlterModelOptions(
            name='permission',
            options={'verbose_name_plural': 'URL表'},
        ),
        migrations.RemoveField(
            model_name='permission2action2role',
            name='p',
        ),
        migrations.AddField(
            model_name='permission2action',
            name='p',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Permission'),
        ),
        migrations.AddField(
            model_name='permission2action2role',
            name='p2a',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='repository.Permission2Action'),
            preserve_default=False,
        ),
    ]