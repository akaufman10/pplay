# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-27 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_submission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='submission',
            name='read',
            field=models.CharField(choices=[('r', 'read'), ('u', 'unread')], default='u', max_length=1),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
