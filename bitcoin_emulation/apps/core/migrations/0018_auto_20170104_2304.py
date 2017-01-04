# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20170104_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='prev_hash',
            field=models.CharField(default=b'', max_length=500),
        ),
        migrations.AlterField(
            model_name='block',
            name='transactions_hash',
            field=models.CharField(default=b'', max_length=500),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='block',
            field=models.ForeignKey(to='core.Block', null=True),
        ),
    ]
