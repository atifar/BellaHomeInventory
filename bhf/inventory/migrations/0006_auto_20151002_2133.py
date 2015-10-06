# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20151001_2345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='keyword_id',
            new_name='keyword',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='productvariant',
            old_name='color_id',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='productvariant',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='productvariant',
            old_name='size_id',
            new_name='size',
        ),
        migrations.RenameField(
            model_name='productvariant',
            old_name='status_id',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='productvariant',
            old_name='supplier_id',
            new_name='supplier',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='keyword_id',
            new_name='keyword',
        ),
    ]
