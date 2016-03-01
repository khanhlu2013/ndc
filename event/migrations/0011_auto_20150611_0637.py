# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_auto_20150611_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendance_lst',
            field=models.ManyToManyField(related_name='xx', through='event.Attendance', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
