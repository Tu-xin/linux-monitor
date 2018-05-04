# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0014_auto_20180430_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverbasemetric',
            name='cpu_load',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='serverbasemetric',
            name='cputype',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='serverbasemetric',
            name='hostname',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='serverbasemetric',
            name='kernel',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='serverbasemetric',
            name='osname',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='serverbasemetric',
            name='uptime',
            field=models.CharField(max_length=10),
        ),
    ]
