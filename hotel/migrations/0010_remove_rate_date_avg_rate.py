# Generated by Django 3.2.3 on 2021-06-03 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_auto_20210603_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='date_avg_rate',
        ),
    ]
