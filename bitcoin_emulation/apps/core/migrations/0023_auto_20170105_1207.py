# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_block_block_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='transactions_hash',
            field=models.CharField(default=b'0', max_length=500),
        ),
    ]
