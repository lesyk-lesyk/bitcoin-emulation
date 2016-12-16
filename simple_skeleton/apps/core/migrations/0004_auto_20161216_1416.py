# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_userinfo_checksum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='login_hash',
            new_name='email_hash',
        ),
    ]
