# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_monitor_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='monitors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('servername', models.CharField(max_length=30)),
                ('item', models.CharField(max_length=30)),
                ('value', models.CharField(default=b'', max_length=30)),
                ('serverip', models.GenericIPAddressField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='monitor',
        ),
    ]
