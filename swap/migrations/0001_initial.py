# Generated by Django 5.1.3 on 2025-01-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('shift_id', models.AutoField(primary_key=True, serialize=False)),
                ('shift_duration', models.IntegerField()),
                ('shift_timing', models.CharField(max_length=50)),
                ('shift_day', models.CharField(max_length=50)),
                ('shift_priority', models.IntegerField()),
            ],
        ),
    ]
