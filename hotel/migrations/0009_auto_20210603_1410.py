# Generated by Django 3.2.3 on 2021-06-03 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_alter_servicehotel_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_rate', models.DecimalField(decimal_places=1, max_digits=3)),
                ('date_avg_rate', models.DateField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.typeservice')),
            ],
            options={
                'get_latest_by': ['date_avg_rate'],
            },
        ),
        migrations.AddConstraint(
            model_name='rate',
            constraint=models.CheckConstraint(check=models.Q(('avg_rate__gte', 0), ('avg_rate__lte', 10)), name='avg_rate_gte_lte'),
        ),
    ]
