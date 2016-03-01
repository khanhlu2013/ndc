# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20150604_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendance_lst',
            field=models.ManyToManyField(related_name='attend_event_lst', through='event.Attendance', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event_rate',
            name='event',
            field=models.ForeignKey(related_name='event_rate_lst', to='event.Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event_rate',
            name='rate',
            field=models.IntegerField(choices=[(0, b'Member dance only'), (1, b'Member lesson and dance'), (2, b'Non-member dance only'), (3, b'Non-member lesson and dance'), (4, b'Tips for blues'), (5, b'UC Santa Cruz student'), (6, b'Exempt'), (7, b'DJ / Instructor'), (8, b'Volunteer')]),
            preserve_default=True,
        ),
    ]
