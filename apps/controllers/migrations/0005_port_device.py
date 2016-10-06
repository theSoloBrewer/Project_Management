# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0001_initial'),
        ('controllers', '0004_auto_20151202_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='port',
            name='device',
            field=models.ForeignKey(default=b'', to='hardware.Hardware'),
        ),
    ]
