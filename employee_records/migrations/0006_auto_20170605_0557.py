# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 02:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_records', '0005_remove_task_assigned_to_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]