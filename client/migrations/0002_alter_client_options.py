# Generated by Django 5.1.1 on 2024-10-15 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['-id']},
        ),
    ]
