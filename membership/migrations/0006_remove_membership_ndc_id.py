# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0005_membership_ndc_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='ndc_id',
        ),
    ]
