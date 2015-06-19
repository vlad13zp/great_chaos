# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=200)),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ParseUrls',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('urls', models.CharField(max_length=200)),
                ('id_url', models.ForeignKey(to='messcover.CrawlUrl')),
            ],
        ),
    ]
