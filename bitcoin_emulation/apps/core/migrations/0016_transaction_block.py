# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20170104_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='block',
            field=models.ForeignKey(default=0, to='core.Block'),
            preserve_default=False,
        ),
    ]
