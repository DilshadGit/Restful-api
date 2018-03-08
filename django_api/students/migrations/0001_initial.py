# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('student_id', models.CharField(blank=True, max_length=9, null=True)),
                ('bio', models.CharField(blank=True, max_length=255, null=True)),
                ('course_title', models.CharField(choices=[('BFS', 'Biomedical and Forensic Sciences'), ('EBE', 'Engineering and the Built Environment'), ('CTG', 'Computing and Technology'), ('LS', 'Life Sciences'), ('PS', 'Psychology')], max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created_date',),
            },
        ),
    ]
