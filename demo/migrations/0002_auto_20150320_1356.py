# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='prize_money',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='audience',
            field=models.CharField(max_length=255, choices=[(b'public', b'\xc3\x96ffentlich'), (b'private', b'Geschlossene Gesellschaft')]),
            preserve_default=True,
        ),
    ]
