# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0003_auto_20150517_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='start_date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
