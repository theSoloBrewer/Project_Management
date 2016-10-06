# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cameras', '0003_auto_20151202_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='network',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='apps.NetworkInfo'),
        ),
    ]
