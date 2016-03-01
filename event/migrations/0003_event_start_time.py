# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_user_lst'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.time(0, 0)),
            preserve_default=False,
        ),
    ]
