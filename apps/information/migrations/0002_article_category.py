# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-28 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[(b'gl', '\u7559\u5b66\u653b\u7565'), (b'lt', '\u7559\u5b66\u8bba\u575b'), (b'zx', '\u7559\u5b66\u54a8\u8be2')], max_length=6, null=True, verbose_name='\u5206\u7c7b'),
        ),
    ]
