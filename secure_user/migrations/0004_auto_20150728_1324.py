# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secure_user', '0003_auto_20150728_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='_first_name',
            field=models.TextField(db_column='first_name', null=True, blank=True),
        ),
    ]
