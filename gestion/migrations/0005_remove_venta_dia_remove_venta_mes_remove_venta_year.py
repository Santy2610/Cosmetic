# Generated by Django 5.0.7 on 2024-08-31 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_venta_dia_venta_mes_venta_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='dia',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='mes',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='year',
        ),
    ]