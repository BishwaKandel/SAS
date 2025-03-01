# Generated by Django 5.0.10 on 2025-03-01 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configure', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_id', models.CharField(max_length=50)),
                ('shift_duration', models.IntegerField()),
                ('shift_timing', models.CharField(max_length=50)),
                ('day', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'unique_together': {('shift_id', 'day')},
            },
        ),
        migrations.CreateModel(
            name='ShiftSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configure.employee')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swap.shift')),
            ],
            options={
                'unique_together': {('shift', 'employee')},
            },
        ),
    ]
