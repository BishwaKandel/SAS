# Generated by Django 5.1.3 on 2025-02-11 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swap', '0009_alter_shift_shift_id_shiftschedule'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='shiftschedule',
            unique_together={('day', 'shift')},
        ),
    ]
