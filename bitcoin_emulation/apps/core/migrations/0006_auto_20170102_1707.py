# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170102_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='private_key',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='public_key',
            field=models.CharField(max_length=100),
        ),
    ]
