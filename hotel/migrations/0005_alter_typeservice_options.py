# Generated by Django 3.2.3 on 2021-05-27 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_alter_servicehotel_mark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typeservice',
            options={'ordering': ['title']},
        ),
    ]