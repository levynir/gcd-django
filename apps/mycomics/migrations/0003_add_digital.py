# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-05 19:01


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycomics', '0002_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='digital_used',
            field=models.BooleanField(default=False, verbose_name='track digitial versions'),
        ),
        migrations.AddField(
            model_name='collection',
            name='rating_used',
            field=models.BooleanField(default=False, verbose_name='rate comics'),
        ),
        migrations.AddField(
            model_name='collectionitem',
            name='is_digital',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='collectionitem',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Poor'), (2, '2 - Fair'), (3, '3 - Good'), (4, '4 - Very Good'), (5, '5 - Excellent')], null=True),
        ),
    ]