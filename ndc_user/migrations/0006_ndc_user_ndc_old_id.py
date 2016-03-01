# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ndc_user', '0005_remove_ndc_user_id_old'),
    ]

    operations = [
        migrations.AddField(
            model_name='ndc_user',
            name='ndc_old_id',
            field=models.CharField(max_length=10, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
