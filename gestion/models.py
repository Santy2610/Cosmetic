from django.db import models

# Create your models here.


class venta(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=150)
    cantidad = models.IntegerField()
    ganancia = models.FloatField()
    presioc = models.FloatField()
    idalma = models.IntegerField()
