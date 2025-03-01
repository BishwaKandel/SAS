# Generated by Django 5.0.10 on 2025-03-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('e_id', models.IntegerField(primary_key=True, serialize=False)),
                ('e_name', models.CharField(max_length=50)),
                ('no_of_hours_worked', models.IntegerField()),
                ('designation', models.CharField(max_length=50)),
                ('e_gmail', models.EmailField(max_length=100)),
                ('e_priority', models.IntegerField()),
            ],
        ),
    ]
