# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ndc_user', '0003_ndc_user_old_member_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ndc_user',
            name='id_old',
            field=models.CharField(max_length=10, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
