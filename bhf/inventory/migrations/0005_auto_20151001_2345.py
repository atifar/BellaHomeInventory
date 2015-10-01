# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20150930_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='keyword_list',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='keyword_list',
        ),
        migrations.AddField(
            model_name='category',
            name='keyword_id',
            field=models.ManyToManyField(to='inventory.Keyword'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='keyword_id',
            field=models.ManyToManyField(to='inventory.Keyword'),
        ),
    ]
