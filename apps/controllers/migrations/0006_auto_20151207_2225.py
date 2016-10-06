# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controllers', '0005_port_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controller',
            name='ports',
        ),
        migrations.RemoveField(
            model_name='port',
            name='device',
        ),
        migrations.AddField(
            model_name='port',
            name='controller',
            field=models.ForeignKey(to='controllers.Controller', null=True),
        ),
        migrations.AlterField(
            model_name='controller',
            name='network',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='apps.NetworkInfo'),
        ),
    ]
