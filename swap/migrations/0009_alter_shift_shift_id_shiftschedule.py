# Generated by Django 5.1.3 on 2025-02-11 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swap', '0008_remove_shift_shift_day_remove_shift_shift_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='shift_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='ShiftSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swap.shift')),
            ],
        ),
    ]
