# Generated by Django 5.0.7 on 2024-08-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='idalma',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
