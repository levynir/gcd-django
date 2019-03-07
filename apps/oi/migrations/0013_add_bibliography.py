# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-11-04 07:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gcd', '0012_add_bibliography'),
        ('oi', '0012_use_creator_and_sort_name_in_creatornamedetailrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='BiblioEntryRevision',
            fields=[
                ('storyrevision_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='oi.StoryRevision')),
                ('page_began', models.IntegerField(blank=True, null=True)),
                ('page_ended', models.IntegerField(blank=True, null=True)),
                ('abstract', models.TextField(blank=True)),
                ('doi', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-created', '-id'],
                'db_table': 'oi_biblio_entry_revision',
            },
            bases=('oi.storyrevision',),
        ),
        migrations.AddField(
            model_name='seriesrevision',
            name='has_about_comics',
            field=models.BooleanField(default=False),
        ),
    ]