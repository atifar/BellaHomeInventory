# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cs_cart', '0002_auto_20150929_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cscartcategory',
            name='keyword_list',
            field=models.CharField(max_length=1500, blank=True),
        ),
        migrations.AlterField(
            model_name='cscartcategory',
            name='meta_description',
            field=models.CharField(max_length=1200, blank=True),
        ),
        migrations.AlterField(
            model_name='cscartproduct',
            name='extra_shipping_cost',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cscartproduct',
            name='keyword_list',
            field=models.CharField(max_length=1500, blank=True),
        ),
        migrations.AlterField(
            model_name='cscartproduct',
            name='list_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cscartproduct',
            name='meta_description',
            field=models.CharField(max_length=1200, blank=True),
        ),
        migrations.AlterField(
            model_name='cscartproduct',
            name='prod_variant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True, to='inventory.ProductVariant'),
        ),
        migrations.AlterField(
            model_name='cscartsubcategory',
            name='keyword_list',
            field=models.CharField(max_length=1500, blank=True),
        ),
        migrations.AlterField(
            model_name='cscartsubcategory',
            name='meta_description',
            field=models.CharField(max_length=1200, blank=True),
        ),
    ]
