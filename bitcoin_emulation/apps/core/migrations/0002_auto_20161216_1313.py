# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='login_hash',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='pass_hash',
            field=models.CharField(default=datetime.datetime(2016, 12, 16, 13, 13, 54, 925573, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
