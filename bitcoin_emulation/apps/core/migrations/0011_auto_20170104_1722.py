# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0010_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='keyPair',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('private', models.IntegerField(default=0)),
                ('public', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='private_key',
            new_name='some_field',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='public_key',
        ),
    ]
