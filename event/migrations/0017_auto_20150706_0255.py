# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0016_auto_20150617_1759'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('date', 'venue')]),
        ),
    ]
