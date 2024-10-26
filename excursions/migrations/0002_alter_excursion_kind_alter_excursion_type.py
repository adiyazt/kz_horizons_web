# Generated by Django 5.0.1 on 2024-05-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion',
            name='kind',
            field=models.CharField(default=('2', 'Лечевно-оздоровительная'), max_length=32, verbose_name='Тип экскурсии'),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='type',
            field=models.CharField(default=('2', 'Групповая'), max_length=32, verbose_name='Тип экскурсии'),
        ),
    ]
