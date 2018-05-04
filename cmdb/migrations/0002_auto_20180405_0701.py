# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='zoneid',
        ),
        migrations.AddField(
            model_name='information',
            name='IDCid',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AddField(
            model_name='information',
            name='locate',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
