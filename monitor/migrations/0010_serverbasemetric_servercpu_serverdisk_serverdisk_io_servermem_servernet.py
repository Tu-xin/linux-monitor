# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0009_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerBaseMetric',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'ID')),
                ('ip', models.GenericIPAddressField()),
                ('hostname', models.CharField(max_length=45)),
                ('cpu_load', models.CharField(max_length=45)),
                ('kernel', models.CharField(max_length=45)),
                ('osname', models.CharField(max_length=45)),
                ('uptime', models.CharField(max_length=45)),
                ('cputype', models.CharField(max_length=45)),
                ('datatime', models.CharField(default=b'null', max_length=20)),
            ],
            options={
                'db_table': 'server_metric',
            },
        ),
        migrations.CreateModel(
            name='ServerCpu',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'ID')),
                ('ip', models.GenericIPAddressField()),
                ('hostname', models.CharField(max_length=45)),
                ('usage_cpu', models.CharField(max_length=30)),
                ('idle_cpu', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'cpu_metric',
            },
        ),
        migrations.CreateModel(
            name='ServerDisk',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'ID')),
                ('ip', models.GenericIPAddressField()),
                ('hostname', models.CharField(max_length=45)),
                ('datatime', models.CharField(default=b'null', max_length=20)),
                ('disk', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'disk_metric',
            },
        ),
        migrations.CreateModel(
            name='ServerDisk_io',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'ID')),
                ('ip', models.GenericIPAddressField()),
                ('dev', models.CharField(max_length=10)),
                ('r_io', models.CharField(max_length=10)),
                ('w_io', models.CharField(max_length=10)),
                ('datatime', models.CharField(default=b'0', max_length=20)),
            ],
            options={
                'db_table': 'disk_io_metric',
            },
        ),
        migrations.CreateModel(
            name='ServerMem',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'ID')),
                ('ip', models.GenericIPAddressField()),
                ('hostname', models.CharField(max_length=45)),
                ('swap_total', models.CharField(max_length=10)),
                ('swap_used', models.CharField(max_length=10)),
                ('swap_free', models.CharField(max_length=10)),
                ('mem_total', models.CharField(max_length=10)),
                ('mem_used', models.CharField(max_length=10)),
                ('mem_free', models.CharField(max_length=10)),
                ('mem_buff', models.CharField(max_length=10)),
                ('mem_use_percent', models.CharField(max_length=10)),
                ('datatime', models.CharField(default=b'0', max_length=20)),
            ],
            options={
                'db_table': 'mem_metric',
            },
        ),
        migrations.CreateModel(
            name='ServerNet',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'ID')),
                ('ip', models.GenericIPAddressField()),
                ('iface', models.CharField(max_length=10)),
                ('traffic_in', models.CharField(max_length=10)),
                ('traffic_out', models.CharField(max_length=10)),
                ('datatime', models.CharField(default=b'0', max_length=20)),
            ],
            options={
                'db_table': 'net_metric',
            },
        ),
    ]
