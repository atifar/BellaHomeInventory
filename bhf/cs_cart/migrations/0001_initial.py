# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsCartCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('page_title', models.CharField(max_length=200)),
                ('meta_description', models.CharField(max_length=500)),
                ('keyword_list', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=100)),
                ('category_id', models.ForeignKey(to='inventory.Category')),
            ],
        ),
        migrations.CreateModel(
            name='CsCartProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('list_price', models.FloatField()),
                ('page_title', models.CharField(max_length=200)),
                ('meta_description', models.CharField(max_length=500)),
                ('keyword_list', models.CharField(max_length=500)),
                ('extra_shipping_cost', models.FloatField()),
                ('prod_variant_id', models.ForeignKey(to='inventory.ProductVariant')),
            ],
        ),
        migrations.CreateModel(
            name='CsCartSubcategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('page_title', models.CharField(max_length=200)),
                ('meta_description', models.CharField(max_length=500)),
                ('keyword_list', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=100)),
                ('category_id', models.ForeignKey(to='inventory.Subcategory')),
            ],
        ),
    ]
