# Generated by Django 5.1.1 on 2024-10-16 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_order', '0008_alter_serviceorder_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceorder',
            name='cpf',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]