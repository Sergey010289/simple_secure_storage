# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='_private_number',
            field=models.CharField(db_column='private_number', null=True, max_length=80, blank=True),
        ),
        migrations.AddField(
            model_name='document',
            name='_summary',
            field=models.CharField(db_column='summary', null=True, max_length=255, blank=True),
        ),
    ]
