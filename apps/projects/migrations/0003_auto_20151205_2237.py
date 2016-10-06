# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20151205_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='lat',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='lng',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True),
        ),
    ]
