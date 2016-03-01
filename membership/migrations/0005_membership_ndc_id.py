# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_auto_20150517_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='ndc_id',
            field=models.CharField(default='P-100', max_length=10),
            preserve_default=False,
        ),
    ]
