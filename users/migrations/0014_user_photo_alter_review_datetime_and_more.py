# Generated by Django 5.0.1 on 2024-06-04 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_review_datetime_alter_update_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.CharField(default='img/images/no-photo.jpg', max_length=128),
        ),
        migrations.AlterField(
            model_name='review',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 21, 33, 12, 983142)),
        ),
        migrations.AlterField(
            model_name='update',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 21, 33, 12, 983142)),
        ),
    ]
