# Generated by Django 3.0.7 on 2021-02-22 04:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0005_auto_20210113_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitemlabel',
            name='height',
            field=models.FloatField(default=20, help_text='Label height, specified in mm', validators=[django.core.validators.MinValueValidator(2)], verbose_name='Height [mm]'),
        ),
        migrations.AddField(
            model_name='stockitemlabel',
            name='width',
            field=models.FloatField(default=50, help_text='Label width, specified in mm', validators=[django.core.validators.MinValueValidator(2)], verbose_name='Width [mm]'),
        ),
        migrations.AddField(
            model_name='stocklocationlabel',
            name='height',
            field=models.FloatField(default=20, help_text='Label height, specified in mm', validators=[django.core.validators.MinValueValidator(2)], verbose_name='Height [mm]'),
        ),
        migrations.AddField(
            model_name='stocklocationlabel',
            name='width',
            field=models.FloatField(default=50, help_text='Label width, specified in mm', validators=[django.core.validators.MinValueValidator(2)], verbose_name='Width [mm]'),
        ),
    ]
