# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-09 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_book_pubtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('gender', models.IntegerField(default=1)),
            ],
        ),
    ]
