# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_auto_20150611_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendance_lst',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='event.Attendance', blank=True),
            preserve_default=True,
        ),
    ]
