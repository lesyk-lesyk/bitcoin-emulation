# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_transaction_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='keypair',
            name='status',
            field=models.CharField(default=b'active', max_length=50),
        ),
        migrations.AddField(
            model_name='transaction',
            name='status',
            field=models.CharField(default=b'pending', max_length=50),
        ),
    ]
