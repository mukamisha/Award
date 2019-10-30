# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-30 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Awar_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='content',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AddField(
            model_name='image',
            name='design',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AddField(
            model_name='image',
            name='link',
            field=models.URLField(default=django.utils.timezone.now, max_length=700),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='usability',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AddField(
            model_name='image',
            name='vote_submissions',
            field=models.IntegerField(default=0),
        ),
    ]
