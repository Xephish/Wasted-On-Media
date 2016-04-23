# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-23 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wastedonmedia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='duration',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='lyrics',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='country',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='director',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='duration',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='synopsis',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='chapters',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='country',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='director',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='duration',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='genre',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='season',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='synopsis',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='country',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='group',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]