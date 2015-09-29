# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('keyword_list', models.TextField(max_length=1500, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_file', models.ImageField(upload_to='')),
                ('thumbnail_file', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity_on_hand', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('short_description', models.TextField(max_length=250, blank=True)),
                ('special_order', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upc', models.IntegerField()),
                ('weight', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('msrp', models.FloatField()),
                ('color_id', models.ForeignKey(to='inventory.Color')),
                ('image', models.ManyToManyField(to='inventory.Image')),
                ('product_id', models.ForeignKey(to='inventory.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size_code', models.CharField(max_length=100, blank=True)),
                ('width', models.CharField(max_length=100, blank=True)),
                ('height', models.CharField(max_length=100, blank=True)),
                ('depth', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('keyword_list', models.TextField(max_length=1500, blank=True)),
                ('category_id', models.ForeignKey(to='inventory.Category')),
                ('image', models.ManyToManyField(to='inventory.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('fax', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='productvariant',
            name='size_id',
            field=models.ForeignKey(to='inventory.Size'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='status_id',
            field=models.ForeignKey(to='inventory.Status'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='supplier_id',
            field=models.ForeignKey(to='inventory.Supplier'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='product_id',
            field=models.ForeignKey(to='inventory.ProductVariant'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ManyToManyField(to='inventory.Image'),
        ),
    ]
