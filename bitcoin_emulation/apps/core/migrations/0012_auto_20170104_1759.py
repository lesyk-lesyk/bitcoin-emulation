# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20170104_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
