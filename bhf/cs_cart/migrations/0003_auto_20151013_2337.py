# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cs_cart', '0002_auto_20151006_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cscartproduct',
            name='prod_variant',
            field=models.ForeignKey(to='inventory.ProductVariant', default=1),
            preserve_default=False,
        ),
    ]
