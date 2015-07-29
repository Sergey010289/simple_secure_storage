# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secure_user', '0005_auto_20150728_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='_last_name',
            field=models.CharField(blank=True, null=True, max_length=255, db_column='last_name'),
        ),
    ]
