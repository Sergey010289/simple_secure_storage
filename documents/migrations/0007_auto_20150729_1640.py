# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20150729_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
