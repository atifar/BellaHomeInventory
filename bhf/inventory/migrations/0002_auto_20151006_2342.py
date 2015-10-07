# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='thumbnail_file',
            field=models.ImageField(upload_to=inventory.models.upload_handler, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, to='inventory.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ManyToManyField(blank=True, to='inventory.Subcategory'),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='image',
            field=models.ManyToManyField(blank=True, to='inventory.Image'),
        ),
    ]
