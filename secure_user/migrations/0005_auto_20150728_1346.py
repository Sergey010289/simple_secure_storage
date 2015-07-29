# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secure_user', '0004_auto_20150728_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='_first_name',
            field=models.CharField(null=True, db_column='first_name', max_length=255, blank=True),
        ),
    ]
