# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0017_auto_20150706_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='duration',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2015, 7, 6, 21, 14, 7, 139342, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
