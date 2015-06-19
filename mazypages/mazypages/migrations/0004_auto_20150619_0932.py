# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mazypages', '0003_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='end_route',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='route',
            name='start_route',
            field=models.URLField(),
        ),
    ]
