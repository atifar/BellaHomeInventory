# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import inventory.models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1200)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('image_file', models.ImageField(upload_to=inventory.models.upload_handler, blank=True)),
                ('thumbnail_file', models.ImageField(upload_to='', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('quantity_on_hand', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('short_description', models.TextField(blank=True, max_length=250)),
                ('special_order', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='inventory.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('upc', models.IntegerField(blank=True, null=True)),
                ('weight', models.CharField(blank=True, max_length=100)),
                ('code', models.CharField(blank=True, max_length=100)),
                ('msrp', models.FloatField(default=0)),
                ('color', models.ForeignKey(to='inventory.Color', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True)),
                ('image', models.ManyToManyField(to='inventory.Image')),
                ('product', models.ForeignKey(to='inventory.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('size_code', models.CharField(blank=True, max_length=100)),
                ('width', models.CharField(blank=True, max_length=100)),
                ('length', models.CharField(blank=True, max_length=100)),
                ('depth', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1200)),
                ('category', models.ForeignKey(to='inventory.Category')),
                ('image', models.ManyToManyField(to='inventory.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('phone', models.IntegerField(blank=True)),
                ('fax', models.IntegerField(blank=True)),
                ('email', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='productvariant',
            name='size',
            field=models.ForeignKey(to='inventory.Size', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='status',
            field=models.ForeignKey(to='inventory.Status'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='supplier',
            field=models.ManyToManyField(to='inventory.Supplier'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ManyToManyField(to='inventory.Subcategory'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='product',
            field=models.OneToOneField(to='inventory.ProductVariant'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ManyToManyField(to='inventory.Image'),
        ),
    ]
