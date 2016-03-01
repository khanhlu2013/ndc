# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_auto_20150611_0637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='attendance_lst',
            new_name='attend_user_lst',
        ),
    ]
