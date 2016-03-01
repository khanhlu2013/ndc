# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_auto_20150517_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(related_name='membership_lst', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
