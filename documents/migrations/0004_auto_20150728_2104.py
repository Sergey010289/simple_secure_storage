# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20150728_2048'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='documentpermission',
            unique_together=set([('document', 'user')]),
        ),
    ]
