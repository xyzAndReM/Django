# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_question_question_text3'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]