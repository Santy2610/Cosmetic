from django.db import models

# Create your models here.


class almacenb(models.Model):
    descripcion = models.CharField(max_length=150)
    numinver = models.IntegerField()
    presioc = models.FloatField()
    presiob = models.FloatField()
    ganancia = models.FloatField()
    cantidad = models.IntegerField()
