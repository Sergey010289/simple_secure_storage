# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import documents.validators


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20150728_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='uploads/', validators=[documents.validators.validate_file]),
        ),
    ]
