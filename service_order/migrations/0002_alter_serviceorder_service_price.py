# Generated by Django 5.1.1 on 2024-10-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceorder',
            name='service_price',
            field=models.CharField(max_length=255),
        ),
    ]
