# Generated by Django 4.1.2 on 2022-11-07 00:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_usercondition_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2022, 11, 7, 0, 20, 42, 621359, tzinfo=datetime.timezone.utc))),
                ('weight', models.FloatField(default=0)),
                ('height', models.FloatField(default=0)),
                ('hip', models.PositiveIntegerField(default=0)),
                ('waist', models.PositiveIntegerField(default=0)),
                ('minimum_pressure', models.PositiveIntegerField(default=0)),
                ('maximum_pressure', models.PositiveIntegerField(default=0)),
                ('imc', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'Condicion Fisica',
                'verbose_name_plural': 'Condiciones Fisicas',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='condition',
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='UserCondition',
        ),
        migrations.AddField(
            model_name='status',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
