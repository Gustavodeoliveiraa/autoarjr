# Generated by Django 5.1.1 on 2024-10-23 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_order', '0016_alter_serviceorder_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='serviceorder',
            name='service',
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='service',
            field=models.ManyToManyField(related_name='service_order', to='service_order.service'),
        ),
    ]
