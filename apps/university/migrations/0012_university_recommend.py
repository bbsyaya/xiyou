# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-10 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0011_auto_20170703_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='recommend',
            field=models.IntegerField(choices=[(1, '\u63a8\u8350'), (0, '\u4e0d\u63a8\u8350')], default=0, verbose_name='\u662f\u5426\u63a8\u8350'),
        ),
    ]
