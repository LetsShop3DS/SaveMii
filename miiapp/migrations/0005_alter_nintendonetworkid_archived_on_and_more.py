# Generated by Django 4.1.7 on 2023-10-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miiapp', '0004_blocklist_alter_nintendonetworkid_archived_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nintendonetworkid',
            name='archived_on',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='nintendonetworkid',
            name='refreshed_on',
            field=models.DateTimeField(blank=True),
        ),
    ]
