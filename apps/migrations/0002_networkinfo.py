# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=16, blank=True)),
                ('subnet', models.CharField(max_length=16, blank=True)),
                ('gateway', models.CharField(max_length=16, blank=True)),
                ('vlan', models.CharField(max_length=200, blank=True)),
                ('MAC', models.CharField(max_length=23, blank=True)),
            ],
        ),
    ]
