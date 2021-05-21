# Generated by Django 3.2.3 on 2021-05-21 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0004_auto_20210521_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='data_arrival',
            field=models.DateField(default='', null=True, verbose_name='Дата заезда'),
        ),
        migrations.AlterField(
            model_name='room',
            name='data_departure',
            field=models.DateField(default='', null=True, verbose_name='Дата отъезда'),
        ),
    ]
