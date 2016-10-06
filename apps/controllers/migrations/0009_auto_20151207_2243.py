# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controllers', '0008_controller_description'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='controller',
            unique_together=set([('project', 'number')]),
        ),
    ]
