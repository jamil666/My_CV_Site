# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Photo',
            field=models.ImageField(blank=True, upload_to='cv_site/static/images'),
        ),
    ]