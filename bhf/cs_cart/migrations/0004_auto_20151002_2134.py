# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cs_cart', '0003_auto_20150930_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cscartcategory',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='cscartsubcategory',
            old_name='subcategory_id',
            new_name='subcategory',
        ),
        migrations.RemoveField(
            model_name='cscartproduct',
            name='keyword_list',
        ),
    ]
