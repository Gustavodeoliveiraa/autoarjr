# Generated by Django 5.1.1 on 2024-10-16 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_order', '0006_serviceorder_observation'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceorder',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
