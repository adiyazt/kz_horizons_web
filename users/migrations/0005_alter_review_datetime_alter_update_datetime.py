# Generated by Django 5.0.1 on 2024-05-30 04:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_review_datetime_alter_update_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 30, 9, 36, 34, 555726)),
        ),
        migrations.AlterField(
            model_name='update',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 30, 9, 36, 34, 556723)),
        ),
    ]
