# Generated by Django 5.1.1 on 2024-10-15 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='address',
        ),
    ]
