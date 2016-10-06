# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20151205_2237'),
        ('controllers', '0006_auto_20151207_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='controller',
            name='project',
            field=models.ForeignKey(default=2, to='projects.Project'),
            preserve_default=False,
        ),
    ]
