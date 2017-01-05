# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_keypair_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='public_x',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='public_y',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
