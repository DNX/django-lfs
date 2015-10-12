# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lfs.catalog.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20150427_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertygroup',
            name='uid',
            field=models.CharField(default=lfs.catalog.models.get_unique_id_str, unique=True, max_length=50, editable=False),
        ),
    ]
