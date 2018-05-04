# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_auto_20180328_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ctime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=b'', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
