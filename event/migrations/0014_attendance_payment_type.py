# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0013_auto_20150611_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='payment_type',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Cash'), (1, b'Credit')]),
            preserve_default=True,
        ),
    ]
