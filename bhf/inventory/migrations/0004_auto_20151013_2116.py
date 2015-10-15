# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20151012_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='product',
        ),
        migrations.AddField(
            model_name='productvariant',
            name='quantity_on_hand',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]
