# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0004_remove_tweets_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
