# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20170702_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='public/images/%Y/%m/%d'),
        ),
    ]
