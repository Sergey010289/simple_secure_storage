# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, db_index=True, unique=True)),
                ('password', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserRemoteKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=32)),
                ('user', models.ForeignKey(related_name='remote_key', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
