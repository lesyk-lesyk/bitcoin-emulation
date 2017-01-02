# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170102_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='private_key',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='public_key',
            field=models.IntegerField(default=0),
        ),
    ]
