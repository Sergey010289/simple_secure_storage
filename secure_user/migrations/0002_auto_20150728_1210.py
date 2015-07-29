# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('secure_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='_email',
            field=models.EmailField(max_length=254, default=datetime.datetime(2015, 7, 28, 12, 10, 9, 498923, tzinfo=utc), db_index=True, db_column='email', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='_first_name',
            field=models.TextField(db_column='first_name', null=True, blank=True),
        ),
    ]
