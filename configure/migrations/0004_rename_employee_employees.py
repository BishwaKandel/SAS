# Generated by Django 5.0.10 on 2025-02-26 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configure', '0003_alter_employee_e_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Employees',
        ),
    ]
