# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import documents.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_created=True)),
                ('file', models.FileField(upload_to='/', validators=[documents.validators.validate_file])),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permit', models.CharField(max_length=1, choices=[('R', 'Read'), ('W', 'Write'), ('D', 'Delete')])),
                ('document', models.ForeignKey(related_name='permissions', to='documents.Document')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='documentpermission',
            unique_together=set([('document', 'user', 'permit')]),
        ),
    ]
