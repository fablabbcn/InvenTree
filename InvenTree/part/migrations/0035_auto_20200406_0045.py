# Generated by Django 2.2.10 on 2020-04-06 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0034_auto_20200404_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part',
            old_name='URL',
            new_name='link',
        ),
    ]
