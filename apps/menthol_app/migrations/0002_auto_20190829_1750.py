# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-30 00:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menthol_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment_amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='transfer',
            old_name='transfer_amount',
            new_name='amount',
        ),
    ]
