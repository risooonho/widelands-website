# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-10 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlhelp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='tribe',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='ware',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='worker',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='building',
            name='type',
            field=models.CharField(choices=[(b'P', b'productionsite'), (b'W', b'warehouse'), (b'M', b'militarysite'), (b'T', b'trainingsite'), (b'm', b'market')], max_length=1),
        ),
    ]