# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secure_user', '0002_auto_20150728_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='_first_name',
            field=models.CharField(db_column='first_name', max_length=200, blank=True, null=True),
        ),
    ]
