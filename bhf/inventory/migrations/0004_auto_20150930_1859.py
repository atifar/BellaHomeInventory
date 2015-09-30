# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20150930_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ManyToManyField(to='inventory.Subcategory'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=1200),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='thumbnail_file',
            field=models.ImageField(upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='quantity_on_hand',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='code',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='color_id',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Color'),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='msrp',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='size_id',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Size'),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='weight',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='description',
            field=models.TextField(max_length=1200),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='fax',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
    ]
