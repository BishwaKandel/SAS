# Generated by Django 5.1.3 on 2025-01-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configure', '0002_rename_e_email_employee_e_gmail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='e_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
