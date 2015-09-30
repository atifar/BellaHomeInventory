# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20150929_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='size',
            old_name='height',
            new_name='length',
        ),
    ]
