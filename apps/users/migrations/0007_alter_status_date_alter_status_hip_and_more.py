# Generated by Django 4.1.2 on 2022-11-07 00:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_status_remove_user_condition_user_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 7, 0, 23, 12, 345736, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='hip',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='status',
            name='maximum_pressure',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='status',
            name='minimum_pressure',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='status',
            name='waist',
            field=models.FloatField(default=0),
        ),
    ]
