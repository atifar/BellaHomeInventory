# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsCartCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('page_title', models.CharField(max_length=200)),
                ('meta_description', models.CharField(max_length=1200, blank=True)),
                ('category', models.OneToOneField(to='inventory.Category')),
            ],
        ),
        migrations.CreateModel(
            name='CsCartProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('list_price', models.FloatField(default=0)),
                ('page_title', models.CharField(max_length=200)),
                ('meta_description', models.CharField(max_length=1200, blank=True)),
                ('extra_shipping_cost', models.FloatField(default=0)),
                ('prod_variant_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='inventory.ProductVariant')),
            ],
        ),
        migrations.CreateModel(
            name='CsCartSubcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('page_title', models.CharField(max_length=200)),
                ('meta_description', models.CharField(max_length=1200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('word', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='cscartsubcategory',
            name='keyword',
            field=models.ManyToManyField(to='cs_cart.Keyword'),
        ),
        migrations.AddField(
            model_name='cscartsubcategory',
            name='status',
            field=models.ForeignKey(to='inventory.Status'),
        ),
        migrations.AddField(
            model_name='cscartsubcategory',
            name='subcategory',
            field=models.OneToOneField(to='inventory.Subcategory'),
        ),
        migrations.AddField(
            model_name='cscartcategory',
            name='keyword',
            field=models.ManyToManyField(to='cs_cart.Keyword'),
        ),
        migrations.AddField(
            model_name='cscartcategory',
            name='status',
            field=models.ForeignKey(to='inventory.Status'),
        ),
    ]
