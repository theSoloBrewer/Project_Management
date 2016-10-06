# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_networkinfo'),
        ('cameras', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camera',
            name='gateway',
        ),
        migrations.RemoveField(
            model_name='camera',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='camera',
            name='subnet',
        ),
        migrations.AddField(
            model_name='camera',
            name='network',
            field=models.ForeignKey(blank=True, to='apps.NetworkInfo', null=True),
        ),
    ]
