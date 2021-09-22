# Generated by Django 3.2 on 2021-09-22 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmea_form', '0005_alter_fmeaprocess_occurence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fmeaprocess',
            name='occurence',
            field=models.IntegerField(choices=[(10, 'More than once per day'), (9, 'Once every 3-4 days'), (8, 'Once Every week'), (7, 'Once every month'), (6, 'Once every 3 months'), (5, 'Once every 6 months'), (4, 'Once a year')], default=0),
        ),
    ]
