# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('hardware', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('installed', models.BooleanField(default=False)),
                ('serial', models.CharField(max_length=200, blank=True)),
                ('ip_address', models.CharField(max_length=16, blank=True)),
                ('subnet', models.CharField(max_length=16, blank=True)),
                ('gateway', models.CharField(max_length=16, blank=True)),
                ('description', models.CharField(max_length=200, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('device', models.ForeignKey(default=b'', to='hardware.Hardware')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
        ),
    ]
