# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-04 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ballot', '0002_auto_20171203_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormatedResultsRow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formated_row', models.CharField(max_length=1000)),
            ],
        ),
    ]
