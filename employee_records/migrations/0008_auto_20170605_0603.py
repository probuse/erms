# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 03:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_records', '0007_auto_20170605_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_records.Employee'),
        ),
    ]
