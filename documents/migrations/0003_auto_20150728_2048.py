# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20150728_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentpermission',
            name='can_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='documentpermission',
            name='can_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='documentpermission',
            name='can_update',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='documentpermission',
            unique_together=set([('document', 'user', 'can_read', 'can_update', 'can_delete')]),
        ),
        migrations.RemoveField(
            model_name='documentpermission',
            name='permit',
        ),
    ]
