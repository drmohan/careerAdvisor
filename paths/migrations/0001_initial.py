# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinkEntries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_url', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=250)),
                ('usr_title', models.CharField(max_length=250)),
                ('usr_headline', models.CharField(max_length=250)),
                ('usr_contact', models.CharField(max_length=250)),
                ('usr_summary', models.CharField(max_length=1000)),
                ('usr_eligibility', models.CharField(max_length=1000)),
                ('usr_additional_info', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='linkentries',
            name='usr_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paths.Users'),
        ),
    ]
