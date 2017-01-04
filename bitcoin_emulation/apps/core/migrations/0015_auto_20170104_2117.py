# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20170104_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='prev_hash',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='block',
            name='transactions_hash',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='input',
            name='address_x',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='input',
            name='address_y',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='input',
            name='signature_r',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='input',
            name='signature_s',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='keypair',
            name='private',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='keypair',
            name='public_x',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='keypair',
            name='public_y',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='output',
            name='address_x',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='output',
            name='address_y',
            field=models.CharField(max_length=500),
        ),
    ]
