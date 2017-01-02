# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20161216_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='email_hash',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='pass_hash',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='private_key',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='public_key',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
