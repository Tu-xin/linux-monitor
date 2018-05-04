# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0015_auto_20180430_0427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servercpu',
            name='hostname',
        ),
        migrations.RemoveField(
            model_name='serverdisk',
            name='hostname',
        ),
        migrations.RemoveField(
            model_name='servermem',
            name='hostname',
        ),
    ]
