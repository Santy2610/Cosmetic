# Generated by Django 3.2.12 on 2024-07-13 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0004_auto_20240713_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='almacenb',
            name='idinver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='almacen.inversion'),
            preserve_default=False,
        ),
    ]
