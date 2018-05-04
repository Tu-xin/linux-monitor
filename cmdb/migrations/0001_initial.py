# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('privateip', models.GenericIPAddressField()),
                ('publicip', models.GenericIPAddressField()),
                ('use', models.TextField()),
                ('zoneid', models.CharField(max_length=30)),
                ('cpu', models.CharField(max_length=50)),
                ('memory', models.CharField(max_length=50)),
                ('datadisk', models.CharField(max_length=30)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
