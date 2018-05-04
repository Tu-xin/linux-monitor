# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20180405_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='os',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
