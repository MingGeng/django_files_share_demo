# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('DownloadDocount', models.IntegerField(verbose_name='Check times', default=0)),
                ('code', models.CharField(verbose_name='code', max_length=8)),
                ('Datatime', models.DateTimeField(verbose_name='add time', default=datetime.datetime.now)),
                ('path', models.CharField(verbose_name='download path', max_length=32)),
                ('name', models.CharField(verbose_name='file name', default='', max_length=32)),
                ('Filesize', models.CharField(verbose_name='file size', max_length=10)),
                ('PCIP', models.CharField(verbose_name='IP address', default='', max_length=32)),
            ],
            options={
                'verbose_name': 'download',
                'db_table': 'download',
            },
        ),
    ]
