# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_propertygroup_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpropertyvalue',
            name='property_group',
            field=models.ForeignKey(related_name='property_values', verbose_name='Property group', blank=True, to='catalog.PropertyGroup', null=True),
        ),
    ]
