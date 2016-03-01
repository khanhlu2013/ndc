# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ndc_user', '0002_ndc_user_is_exempt'),
    ]

    operations = [
        migrations.AddField(
            model_name='ndc_user',
            name='old_member_id',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
