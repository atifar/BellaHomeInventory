# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20151006_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='special_order',
        ),
        migrations.AddField(
            model_name='image',
            name='image_alt_text',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='special_order',
            field=models.BooleanField(default=False),
        ),
    ]
