# Generated by Django 5.1.1 on 2024-10-15 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_order', '0002_alter_serviceorder_service_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceorder',
            name='service_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
