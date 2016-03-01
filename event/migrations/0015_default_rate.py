# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0014_attendance_payment_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Default_rate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.IntegerField(choices=[(0, b'Member dance only'), (1, b'Member lesson and dance'), (2, b'Non-member dance only'), (3, b'Non-member lesson and dance'), (4, b'Tips for blues'), (5, b'UC Santa Cruz student'), (6, b'Exempt'), (7, b'DJ / Instructor'), (8, b'Volunteer')])),
                ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
