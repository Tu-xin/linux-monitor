# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0011_auto_20180430_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverbasemetric',
            name='id',
            field=models.IntegerField(default=b'0', serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='servercpu',
            name='id',
            field=models.IntegerField(default=b'0', serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='serverdisk',
            name='id',
            field=models.IntegerField(default=b'0', serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='serverdisk_io',
            name='id',
            field=models.IntegerField(default=b'0', serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='servermem',
            name='id',
            field=models.IntegerField(default=b'0', serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='servernet',
            name='id',
            field=models.IntegerField(default=b'0', serialize=False, primary_key=True),
        ),
    ]
