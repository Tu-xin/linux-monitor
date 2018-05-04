# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0008_auto_20170815_2146'),
    ]

    operations = [
        migrations.DeleteModel(
            name='question',
        ),
    ]
