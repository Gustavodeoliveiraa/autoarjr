# Generated by Django 5.1.1 on 2024-10-21 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_order', '0014_alter_serviceorder_car_plate_alter_serviceorder_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceorder',
            name='created_at',
            field=models.DateField(),
        ),
    ]
