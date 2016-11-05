# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('owner_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alternative1.Group')),
                ('owner_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alternative1.Person')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='alternative1.Person'),
        ),
    ]