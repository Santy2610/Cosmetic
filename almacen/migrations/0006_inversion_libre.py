# Generated by Django 3.2.12 on 2024-07-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0005_almacenb_idinver'),
    ]

    operations = [
        migrations.AddField(
            model_name='inversion',
            name='libre',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
