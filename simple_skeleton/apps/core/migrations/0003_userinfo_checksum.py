# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20161216_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='checksum',
            field=models.CharField(default=datetime.datetime(2016, 12, 16, 13, 29, 9, 578809, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
