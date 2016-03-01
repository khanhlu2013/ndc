# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20150527_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='user_lst',
        ),
    ]
