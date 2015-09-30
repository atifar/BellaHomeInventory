# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20150929_1913'),
        ('cs_cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cscartsubcategory',
            name='category_id',
        ),
        migrations.AddField(
            model_name='cscartsubcategory',
            name='subcategory_id',
            field=models.OneToOneField(to='inventory.Subcategory', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cscartcategory',
            name='category_id',
            field=models.OneToOneField(to='inventory.Category'),
        ),
    ]
