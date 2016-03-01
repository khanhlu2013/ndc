# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_remove_event_user_lst'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='paid_amount',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
    ]
