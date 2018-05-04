# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0007_zsj'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='zsj',
            new_name='zaj',
        ),
    ]
