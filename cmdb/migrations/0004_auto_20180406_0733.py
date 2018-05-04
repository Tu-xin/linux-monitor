# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_information_os'),
    ]

    operations = [
        migrations.RenameField(
            model_name='information',
            old_name='name',
            new_name='SN',
        ),
    ]
