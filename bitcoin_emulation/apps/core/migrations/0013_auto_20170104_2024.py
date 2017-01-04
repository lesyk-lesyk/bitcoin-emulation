# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20170104_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('prev_hash', models.IntegerField(default=0)),
                ('nonce', models.IntegerField(default=0)),
                ('transactions_hash', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_x', models.IntegerField(default=0)),
                ('address_y', models.IntegerField(default=0)),
                ('signature_r', models.IntegerField(default=0)),
                ('signature_s', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_x', models.IntegerField(default=0)),
                ('address_y', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='output',
            name='transaction',
            field=models.ForeignKey(to='core.Transaction'),
        ),
        migrations.AddField(
            model_name='input',
            name='transaction',
            field=models.ForeignKey(to='core.Transaction'),
        ),
    ]
