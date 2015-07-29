# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('secure_user', '0006_user__last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='_email',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, db_index=True, max_length=254, default=datetime.datetime(2015, 7, 29, 7, 33, 55, 293741, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
