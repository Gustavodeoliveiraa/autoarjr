# Generated by Django 5.1.1 on 2024-10-06 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_alter_storage_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='storage',
            name='detail',
            field=models.CharField(default='', max_length=255),
        ),
    ]
