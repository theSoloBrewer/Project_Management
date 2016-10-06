# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('hardware', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DoorHardware',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('installed', models.BooleanField(default=False)),
                ('door', models.ForeignKey(to='doors.Door')),
                ('hardware', models.ForeignKey(to='hardware.Hardware')),
            ],
        ),
        migrations.AddField(
            model_name='door',
            name='devices',
            field=models.ManyToManyField(to='hardware.Hardware', through='doors.DoorHardware'),
        ),
        migrations.AddField(
            model_name='door',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
        ),
    ]
