# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-02 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_players_played'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='display',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='players',
            name='losses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='players',
            name='wins',
            field=models.IntegerField(default=0),
        ),
    ]
