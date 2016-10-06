# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controllers', '0007_controller_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='controller',
            name='description',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
