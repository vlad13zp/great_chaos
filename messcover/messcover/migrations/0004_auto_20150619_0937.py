# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messcover', '0003_auto_20150619_0933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parseurls',
            name='urls',
        ),
        migrations.AddField(
            model_name='parseurls',
            name='url',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parseurls',
            name='name',
            field=models.CharField(default=b'name url', max_length=200),
        ),
    ]
