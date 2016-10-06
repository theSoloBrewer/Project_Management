# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_networkinfo'),
        ('controllers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Controller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=200)),
                ('serial', models.CharField(max_length=200, blank=True)),
                ('network', models.ForeignKey(to='apps.NetworkInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PortType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='port',
            name='type',
            field=models.ForeignKey(to='controllers.PortType'),
        ),
        migrations.AddField(
            model_name='controller',
            name='ports',
            field=models.ForeignKey(default=b'', to='controllers.Port'),
        ),
    ]
