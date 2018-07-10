# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-10 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xlfile', models.FileField(upload_to='files/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
