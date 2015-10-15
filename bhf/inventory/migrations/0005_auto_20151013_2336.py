# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20151013_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='color',
            field=models.ForeignKey(to='inventory.Color', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='size',
            field=models.ForeignKey(to='inventory.Size', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='fax',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
