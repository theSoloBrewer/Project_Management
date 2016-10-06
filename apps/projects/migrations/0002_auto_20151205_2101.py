# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='lat',
            field=models.DecimalField(default=34.397, max_digits=8, decimal_places=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='lng',
            field=models.DecimalField(default=150.644, max_digits=8, decimal_places=3),
            preserve_default=False,
        ),
    ]
