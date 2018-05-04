# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 28, 8, 13, 49, 804820, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=2, max_length=16),
            preserve_default=False,
        ),
    ]
