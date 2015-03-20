# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.ForeignKey(related_name='user', blank=True, to='demo.Team', null=True),
            preserve_default=True,
        ),
    ]
