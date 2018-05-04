# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0006_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='zsj',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
