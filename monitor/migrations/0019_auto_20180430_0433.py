# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0018_auto_20180430_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverbasemetric',
            name='hostname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='serverbasemetric',
            name='osname',
            field=models.CharField(max_length=20),
        ),
    ]
