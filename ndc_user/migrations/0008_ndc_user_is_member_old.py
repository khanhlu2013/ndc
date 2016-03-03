# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ndc_user', '0007_auto_20160303_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='ndc_user',
            name='is_member_old',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
