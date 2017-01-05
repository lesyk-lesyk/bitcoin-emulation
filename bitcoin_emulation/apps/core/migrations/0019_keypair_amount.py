# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20170104_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='keypair',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
