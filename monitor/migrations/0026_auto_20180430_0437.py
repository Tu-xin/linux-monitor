# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0025_auto_20180430_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverdisk',
            name='disk',
            field=models.CharField(max_length=200),
        ),
    ]
