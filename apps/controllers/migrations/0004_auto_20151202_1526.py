# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controllers', '0003_auto_20151202_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controller',
            name='ports',
            field=models.ForeignKey(to='controllers.Port', blank=True),
        ),
    ]
