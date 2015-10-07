# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20151006_2342'),
        ('cs_cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cscartproduct',
            name='prod_variant_id',
        ),
        migrations.AddField(
            model_name='cscartproduct',
            name='prod_variant',
            field=models.ForeignKey(to='inventory.ProductVariant', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AlterField(
            model_name='cscartcategory',
            name='keyword',
            field=models.ManyToManyField(to='cs_cart.Keyword', blank=True),
        ),
        migrations.AlterField(
            model_name='cscartsubcategory',
            name='keyword',
            field=models.ManyToManyField(to='cs_cart.Keyword', blank=True),
        ),
    ]
