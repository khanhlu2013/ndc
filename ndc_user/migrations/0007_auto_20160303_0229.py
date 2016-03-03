# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ndc_user', '0006_ndc_user_ndc_old_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ndc_user',
            name='membership_type',
        ),
        migrations.RemoveField(
            model_name='ndc_user',
            name='old_member_id',
        ),
    ]
