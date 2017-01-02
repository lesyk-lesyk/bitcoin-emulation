# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170102_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='checksum',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='text',
        ),
    ]
