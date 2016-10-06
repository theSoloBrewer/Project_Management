# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controllers', '0006_auto_20151207_2225'),
        ('doors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doorhardware',
            name='port',
            field=models.ForeignKey(blank=True, to='controllers.Port', null=True),
        ),
    ]
