# Generated by Django 5.1.1 on 2024-10-18 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_order', '0010_alter_serviceorder_car_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceorder',
            name='car_plate',
            field=models.CharField(max_length=20),
        ),
    ]
