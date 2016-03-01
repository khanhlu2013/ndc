# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField()),
                ('membership_type', models.IntegerField(choices=[(0, b'Bronze'), (1, b'Silver'), (2, b'Gold')])),
                ('is_issue_key', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
