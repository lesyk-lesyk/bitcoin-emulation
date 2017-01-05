# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20170105_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='block_hash',
            field=models.CharField(default=b'0', max_length=500),
        ),
    ]
