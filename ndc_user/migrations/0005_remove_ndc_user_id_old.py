# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ndc_user', '0004_ndc_user_id_old'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ndc_user',
            name='id_old',
        ),
    ]
