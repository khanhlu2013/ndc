# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_attendance_paid_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_rate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.IntegerField(choices=[(0, b'Member dance only'), (1, b'Member lesson and dance'), (2, b'None member dance only'), (3, b'None member lesson and dance'), (4, b'Tips for blues'), (5, b'UC Santa Cruz student'), (6, b'Exempt'), (7, b'DJ / Instructor'), (8, b'Volunteer')])),
                ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('event', models.ForeignKey(to='event.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='paid_amount',
        ),
        migrations.AddField(
            model_name='attendance',
            name='event_rate',
            field=models.ForeignKey(default=None, to='event.Event_rate'),
            preserve_default=False,
        ),
    ]
