# Generated by Django 4.1.7 on 2023-10-09 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miiapp', '0008_alter_nintendonetworkid_archived_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nintendonetworkid',
            name='archived_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 9, 16, 9, 16, 814881, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='nintendonetworkid',
            name='rank',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='nintendonetworkid',
            name='refreshed_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 9, 16, 9, 16, 814920, tzinfo=datetime.timezone.utc)),
        ),
    ]
