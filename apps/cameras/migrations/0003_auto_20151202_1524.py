# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras', '0002_auto_20151202_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='network',
            field=models.OneToOneField(null=True, blank=True, to='apps.NetworkInfo'),
        ),
    ]
