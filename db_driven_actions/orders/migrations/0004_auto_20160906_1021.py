# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-06 10:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0003_order_timestamp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['timestamp']},
        ),
        migrations.AddField(
            model_name='orderaction',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderaction',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='orders.Order'),
        ),
    ]