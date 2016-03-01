# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0004_auto_20150526_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('anonymous_first_name', models.CharField(max_length=100, null=True, blank=True)),
                ('anonymous_last_name', models.CharField(max_length=100, null=True, blank=True)),
                ('event', models.ForeignKey(to='event.Event')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='attendance_lst',
            field=models.ManyToManyField(related_name='attend_event_lst', through='event.Attendance', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='user_lst',
            field=models.ManyToManyField(related_name='volunteer_event_lst', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
