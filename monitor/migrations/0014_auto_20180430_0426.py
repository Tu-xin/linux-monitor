# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0013_auto_20180430_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverbasemetric',
            name='cputype',
            field=models.CharField(max_length=10),
        ),
    ]
