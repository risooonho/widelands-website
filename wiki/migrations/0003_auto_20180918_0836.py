# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-18 08:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_auto_20161218_1056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'default_permissions': ('change', 'add'), 'ordering': ['title'], 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='creator_ip',
        ),
        migrations.RemoveField(
            model_name='changeset',
            name='editor_ip',
        ),
    ]
