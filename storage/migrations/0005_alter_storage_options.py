# Generated by Django 5.1.1 on 2024-10-18 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_alter_storage_detail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storage',
            options={'ordering': ['-id']},
        ),
    ]