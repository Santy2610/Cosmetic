# Generated by Django 5.0.7 on 2024-09-03 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0008_remove_pedido_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='fecha',
            field=models.DateField(default=2012),
            preserve_default=False,
        ),
    ]
