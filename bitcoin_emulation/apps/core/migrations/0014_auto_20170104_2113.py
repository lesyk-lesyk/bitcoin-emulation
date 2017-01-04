# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20170104_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keypair',
            old_name='public',
            new_name='public_x',
        ),
        migrations.AddField(
            model_name='keypair',
            name='public_y',
            field=models.IntegerField(default=0),
        ),
    ]
